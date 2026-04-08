"""
AI Engine Module.
Generates insights from simulation data using Groq API.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_ai_insight(simulation_data: dict) -> str:
    """
    Generates contextual insights based on the simulation results.
    
    Args:
        simulation_data (dict): Dictionary holding inputs and output results.
        
    Returns:
        str: A strict 4-6 line explanation of trade-offs and recommendations.
    """
    api_key = os.getenv("GROK_API_KEY")
    if not api_key:
        return "⚠️ API Key missing. Please ensure GROK_API_KEY is set in your .env file."
        
    endpoint = "https://api.groq.com/openai/v1/chat/completions"
    
    prompt = f"""
    You are a Senior System Reliability Architect. Briefly analyze this V&V simulation output:
    
    [Simulation Profile]
    Methodology: {simulation_data.get('testing_type')}
    System Complexity: {simulation_data.get('complexity')}
    Time Budget: {simulation_data.get('time_budget')} days
    
    [Results]
    Bugs Detected: {simulation_data.get('bugs_detected')} out of {simulation_data.get('total_bugs')}
    Total Cost: ${simulation_data.get('cost')}
    Efficiency Score: {simulation_data.get('efficiency_score')}
    Time Utilization: {simulation_data.get('time_utilization')}%
    
    Task:
    1. Explain the observed technical results.
    2. Highlight the trade-off strictly between cost, efficiency, and accuracy derived from the metrics.
    3. Recommend the most optimal testing adjustment.
    
    Constraints:
    - Respond strictly in 4 to 6 lines.
    - Be highly technical but concise.
    - No generic fluff. Reference the metrics directly.
    """
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are a pragmatic, highly technical software testing architect."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=12)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Insight generation failed: {str(e)}.\n\n**Fallback Interpretation**: This configuration yielded an efficiency score of {simulation_data.get('efficiency_score')}. The time utilization is {simulation_data.get('time_utilization')}%. If utilization is low, reduce your time budget or switch methodologies to mitigate setup cost."
