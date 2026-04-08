"""
Core Simulation Engine for V&V Evolution.
Contains mathematical logic for testing methodologies.
"""

def run_simulation(testing_type: str, complexity: int, time_budget: int) -> dict:
    """
    Simulates testing outcomes based on deterministic formulas.
    
    Args:
        testing_type (str): The testing methodology ('Manual', 'Automated', 'AI_Based').
        complexity (int): System complexity level (1=Low, 2=Medium, 3=High).
        time_budget (int): Total allocated days (1 to 20).
    
    Returns:
        dict: A dictionary containing Bugs Detected, Total Bugs, Cost, Efficiency Score, and Time Utilization.
    """
    
    # 1. Define Base Constants per Testing Type
    # Structure: { Type: (Setup Time, Effort Const k_base, Bug Cap m_max, Fixed Cost, Variable Cost) }
    base_values = {
        "Manual": {"t_setup": 0, "k_base": 5.0, "m_max": 0.85, "c_fixed": 0, "c_var": 200},
        "Automated": {"t_setup": 4, "k_base": 2.0, "m_max": 0.70, "c_fixed": 1000, "c_var": 20},
        "AI_Based": {"t_setup": 1, "k_base": 3.0, "m_max": 0.95, "c_fixed": 500, "c_var": 50}
    }
    
    if testing_type not in base_values:
        raise ValueError(f"Unknown testing type: {testing_type}")
        
    vals = base_values[testing_type]
    
    # 2. Define Complexity Multipliers
    # Structure: { Complexity: (Total Bugs tb, Effort Multiplier k_mul, Cost Multiplier cm) }
    comp_multipliers = {
        1: {"tb": 100, "k_mul": 1.0, "cm": 1.0},
        2: {"tb": 250, "k_mul": 1.5, "cm": 1.5},
        3: {"tb": 500, "k_mul": 2.0, "cm": 2.0}
    }
    
    if complexity not in comp_multipliers:
        raise ValueError(f"Unknown complexity level: {complexity}")
        
    c_vals = comp_multipliers[complexity]
    
    # 3. Calculate Effective Execution Time (t_exec)
    # Time actually spent hunting bugs, bounded cleanly at zero.
    t_exec = max(0, time_budget - vals["t_setup"])
    
    # 4. Calculate Final Effort Constant (k)
    # Effort scales up proportionally as system complexity rises.
    k = vals["k_base"] * c_vals["k_mul"]
    
    # 5. Calculate Progress (Diminishing Return Curve)
    # Bounded safely between 0.0 and 1.0 without dividing by zero.
    if (t_exec + k) <= 0:
        progress = 0.0
    else:
        progress = t_exec / (t_exec + k)
        
    # 6. Calculate Bugs Detected
    # Absolute number bounded by the maximum cap of the methodology.
    bugs_detected = c_vals["tb"] * vals["m_max"] * progress
    
    # 7. Calculate Total Cost
    # Fixed costs plus daily variable burn rate, penalized by complexity.
    cost = (vals["c_fixed"] + (vals["c_var"] * time_budget)) * c_vals["cm"]
    
    # 8. Calculate Efficiency (ROI)
    # Metric representing bugs found per $1,000 spent. Safeguarded and capped at 100.
    if cost <= 0:
        efficiency = 0.0
    else:
        efficiency_raw = (bugs_detected / cost) * 1000.0
        efficiency = min(100.0, max(0.0, efficiency_raw))
        
    # 9. Calculate Time Utilization
    # Percentage of the budget that was dynamically productive vs wasted in setup.
    if time_budget <= 0:
        time_utilization = 0.0
    else:
        time_utilization = (t_exec / time_budget) * 100.0
        
    return {
        "bugs_detected": round(bugs_detected, 2),
        "total_bugs": c_vals["tb"],
        "cost": round(cost, 2),
        "efficiency_score": round(efficiency, 2),
        "time_utilization": round(time_utilization, 2)
    }
