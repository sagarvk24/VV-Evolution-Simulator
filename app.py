import streamlit as st
import plotly.graph_objects as go
from simulation import run_simulation

st.set_page_config(
    page_title="V&V Evolution System",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Landing Page Logic
    if 'app_started' not in st.session_state:
        st.session_state['app_started'] = False

    if not st.session_state['app_started']:
        # Centered Layout
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("V&V Evolution Intelligence System")
            st.write("Understand how testing strategies evolve through simulation, visualization, and AI-driven insights.")
            
            st.divider()
            
            st.markdown("### Key Highlights")
            st.markdown("""
            * ⚙️ **Interactive Simulation Engine**
            * 📊 **Dynamic Visual Analysis**
            * 🧠 **AI-Powered Insights**
            """)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("🚀 Start Exploring", type="primary", use_container_width=True):
                st.session_state['app_started'] = True
                st.rerun()
                
        return  # Explicitly halt rendering to prevent the sidebar from appearing

    # Main application renders below this line
    st.sidebar.title("Navigation")
    
    # Sidebar navigation
    pages = ["Home", "Evolution", "Simulation", "Insights"]
    selection = st.sidebar.radio("Go to", pages)
    
    # Routing
    if selection == "Home":
        st.title("💡 Verification & Validation")
        st.write("### Building the system right vs. Building the right system")
        st.write("Software systems fail not just because of bad code, but because of misunderstood requirements or inadequate testing boundaries. Verification and Validation (V&V) form the framework to ensure both quality and exactness.")
        
        st.divider()
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Verification")
            st.info("**Are we building the product right?**")
            st.markdown("""
            * **Objective:** Checks whether the software conforms to its technical specifications.
            * **Activities:** Reviews, Walkthroughs, Inspections, and Static Analysis.
            * **Target:** Architecture, Design, and Code before runtime.
            """)
            
        with c2:
            st.subheader("Validation")
            st.info("**Are we building the right product?**")
            st.markdown("""
            * **Objective:** Checks whether the software meets the user's true functional expectations.
            * **Activities:** Unit Testing, Integration Testing, and User Acceptance Testing (UAT).
            * **Target:** The actual compiled software product executing in real environments.
            """)
            
        st.divider()
        
        st.subheader("🚀 Why Evolution in Testing Was Necessary")
        st.markdown("""
        * **System Complexity:** Modern cloud and structural microservices cannot be fully manually verified due to infinite state permutations.
        * **Cost of Escaped Defects:** A bug found in production costs orders of magnitude more to patch than a defect caught during the design phase.
        * **Deployment Velocity:** Agile and Continuous Integration (CI/CD) pipelines require instant feedback. Manual testing creates unscalable deployment bottlenecks.
        * **The AI Paradigm:** Shifting from strict, rigid automated scripts to AI-assisted dynamic testing allows systems to hunt for undocumented edge cases without linear cost increases.
        """)
        
    elif selection == "Evolution":
        st.title("📈 Evolution of V&V Testing")
        st.write("Explore how Verification and Validation paradigms have shifted to combat increasing system complexity.")
        
        # Navigation/Selection
        evolution_era = st.selectbox("Select Testing Era", ["Traditional (Manual)", "Automated", "AI-Based"])
        
        st.divider()
        
        # Dynamic Content Branching
        if evolution_era == "Traditional (Manual)":
            st.subheader("Human-Driven Verification")
            st.write("Software quality relies entirely on human intuition, exploratory testing, and manual test execution scripts.")
            
            st.markdown("### Key Characteristics")
            st.markdown("""
            * **High Adaptability:** Humans can naturally adapt to unexpected UI changes and unscripted edge cases.
            * **Fatigue Degradation:** The bug detection rate falls off sharply over time due to human bias and exhaustion.
            * **Linear Cost Scaling:** To test twice as fast, you must hire twice as many engineers.
            """)
            
            st.caption("Era Metrics")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric(label="Execution Speed", value="Slow", delta="Limited by human speed", delta_color="off")
            with m2:
                st.metric(label="Accuracy Limit", value="Medium", delta="Misses repetitive patterns", delta_color="off")
            with m3:
                st.metric(label="Cost Structure", value="High Variable", delta="Scales linearly by hour", delta_color="off")
                
        elif evolution_era == "Automated":
            st.subheader("Script-Driven Execution")
            st.write("The introduction of regression test harnesses and Continuous Integration pipelines. Machines execute deterministic rules pre-written by humans.")
            
            st.markdown("### Key Characteristics")
            st.markdown("""
            * **Perfect Consistency:** Does exactly what the script commands, thousands of times, without error or variance.
            * **Brittle Maintenance:** Even a minor graphical change can break hundreds of rigorous UI tests.
            * **Tunnel Vision:** The pipeline cannot detect an obvious catastrophic layout bug if the script wasn't explicitly looking for it.
            """)
            
            st.caption("Era Metrics")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric(label="Execution Speed", value="Extremely Fast", delta="CI/CD velocity", delta_color="normal")
            with m2:
                st.metric(label="Accuracy Limit", value="Strictly Bounded", delta="Only finds programmed bugs", delta_color="off")
            with m3:
                st.metric(label="Cost Structure", value="High Fixed", delta="Low run cost, huge setup", delta_color="normal")
                
        elif evolution_era == "AI-Based":
            st.subheader("Intent-Driven Validation")
            st.write("Machine Learning models actively navigate applications, generating tests and verifying intents semi-autonomously.")
            
            st.markdown("### Key Characteristics")
            st.markdown("""
            * **Self-Healing Code:** Capable of understanding that an element ID completely changed while its underlying purpose survived.
            * **Exploratory Power:** Can actively fuzz and mutate parameters to discover unseen multidimensional edge cases.
            * **Intelligent Insights:** Identifies defects and provides explainable root-cause architectural fixes simultaneously.
            """)
            
            st.caption("Era Metrics")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric(label="Execution Speed", value="Fast", delta="Incurs LLM inference latency", delta_color="off")
            with m2:
                st.metric(label="Accuracy Limit", value="Near-Maximum", delta="Explores unknown logic trees", delta_color="normal")
            with m3:
                st.metric(label="Cost Structure", value="Moderate Hybrid", delta="API Token & Infrastructure Overhead", delta_color="off")
                
    elif selection == "Simulation":
        st.title("Interactive Simulation")
        st.write("Configure inputs below to run the V&V Evaluation Engine.")
        
        # UI Input Controls
        col1, col2, col3 = st.columns(3)
        with col1:
            testing_type = st.selectbox("Testing Methodology", ["Manual", "Automated", "AI_Based"])
        with col2:
            complexity_label = st.selectbox("System Complexity", ["Low", "Medium", "High"])
            complexity_map = {"Low": 1, "Medium": 2, "High": 3}
            complexity = complexity_map[complexity_label]
        with col3:
            time_budget = st.slider("Time Budget (Days)", min_value=1, max_value=20, value=10)
            
        st.divider()
        
        # Run the deterministic logic
        results = run_simulation(testing_type, complexity, time_budget)
        
        # Save state for AI Insights
        st.session_state['last_sim_data'] = {
            "testing_type": testing_type,
            "complexity": complexity_label,
            "time_budget": time_budget,
            **results
        }
        
        st.caption("Results based on selected testing strategy and system conditions")
        # Render the Output
        st.subheader("Simulation Results")
        m1, m2, m3, m4 = st.columns(4)
        
        with m1:
            st.metric("Bugs Detected", f"{results['bugs_detected']} / {results['total_bugs']}")
        with m2:
            st.metric("Total Cost", f"${results['cost']:,.2f}")
        with m3:
            st.metric("Efficiency Score", f"{results['efficiency_score']}")
        with m4:
            st.metric("Time Utilization", f"{results['time_utilization']}%")
            
        st.divider()
        st.subheader("Visual Analysis of Testing Strategies")
        st.info("💡 Observe how Manual testing drops off due to fatigue, while Automated systems incur high initial setup costs before executing.")
        
        # Generate temporal data (Day 1 to Day 20)
        time_range = list(range(1, 21))
        methods = ["Manual", "Automated", "AI_Based"]
        ui_names = {"Manual": "Manual", "Automated": "Automated", "AI_Based": "AI-Based"}
        colors = {"Manual": "#5DADE2", "Automated": "#F5B041", "AI_Based": "#58D68D"}
        
        fig_bugs = go.Figure()
        fig_cost = go.Figure()
        
        for method in methods:
            bugs = []
            costs = []
            for t_val in time_range:
                res = run_simulation(method, complexity, t_val)
                bugs.append(res['bugs_detected'])
                costs.append(res['cost'])
                
            fig_bugs.add_trace(go.Scatter(x=time_range, y=bugs, mode='lines', name=ui_names[method], line=dict(color=colors[method], width=3)))
            fig_cost.add_trace(go.Scatter(x=time_range, y=costs, mode='lines', name=ui_names[method], line=dict(color=colors[method], width=3)))
            
        # Layouts
        fig_bugs.update_layout(title="Bugs Detected vs Time (Diminishing Returns Behavior)", xaxis_title="Time Budget (Days)", yaxis_title="Number of Bugs Detected", margin=dict(l=20, r=20, t=40, b=20))
        fig_cost.update_layout(title="Cost Growth vs Time Across Testing Strategies", xaxis_title="Time Budget (Days)", yaxis_title="Accumulated Cost ($)", margin=dict(l=20, r=20, t=40, b=20))
        
        g1, g2 = st.columns(2)
        with g1:
            st.plotly_chart(fig_bugs, use_container_width=True)
        with g2:
            st.plotly_chart(fig_cost, use_container_width=True)
            
        st.markdown("---")
            
        # Efficiency Bar Chart (Current UI State)
        fig_eff = go.Figure()
        eff_scores = []
        ui_method_list = []
        for method in methods:
            res_eff = run_simulation(method, complexity, time_budget)
            eff_scores.append(res_eff['efficiency_score'])
            ui_method_list.append(ui_names[method])
            
        fig_eff.add_trace(go.Bar(x=ui_method_list, y=eff_scores, marker_color=[colors[m] for m in methods], text=eff_scores, textposition='auto'))
        fig_eff.update_layout(title=f"Efficiency Score Comparison (Snapshot at Day {time_budget})", xaxis_title="Testing Strategy", yaxis_title="Efficiency Score (Bugs per $1,000)", margin=dict(l=20, r=20, t=40, b=20))
        
        st.plotly_chart(fig_eff, use_container_width=True)
        
    elif selection == "Insights":
        st.title("🧠 AI Reasoning Engine (Powered by Llama-3.3-70B-Versatile)")
        st.caption("AI-generated insights based on simulation outputs and system conditions")
        
        st.markdown("---")
        
        if "last_sim_data" not in st.session_state:
            st.warning("⚠️ No simulation data found. Please run a scenario in the 'Simulation' panel first to generate context.")
        else:
            sim_data = st.session_state['last_sim_data']
            ui_names = {"Manual": "Manual", "Automated": "Automated", "AI_Based": "AI-Based"}
            
            # Clear Context Presentation Layout
            st.subheader("Current Simulation Context")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Testing Strategy", ui_names.get(sim_data['testing_type'], sim_data['testing_type']))
            with c2:
                st.metric("System Complexity", sim_data['complexity'])
            with c3:
                st.metric("Time Budget", f"{sim_data['time_budget']} Days")
                
            st.markdown("---")
            
            if st.button("Generate AI Insight", type="primary"):
                with st.spinner("Executing architectural reasoning via Llama-3.3-70b..."):
                    from ai_engine import get_ai_insight
                    insight_text = get_ai_insight(sim_data)
                    
                    st.success("Analysis Complete")
                    
                    # Safely separate the text to prevent any truncation
                    insight_part = insight_text
                    rec_part = ""
                    
                    # Look for common recommendation keywords to split cleanly without deleting characters
                    import re
                    match = re.search(r'(?i)(\bWe recommend\b|\bI recommend\b|\bRecommendation:\b|\bRecommend\b)', insight_text)
                    if match and match.start() > 10:
                        split_idx = match.start()
                        insight_part = insight_text[:split_idx].strip()
                        rec_part = insight_text[split_idx:].strip()
                    else:
                        # Fallback: split by paragraph to avoid dropping sentences
                        if '\n' in insight_text:
                            lines = [line.strip() for line in insight_text.split('\n') if line.strip()]
                            if len(lines) > 1:
                                insight_part = '\n\n'.join(lines[:-1])
                                rec_part = lines[-1]
                        
                    if not rec_part:
                        # Extreme fallback: render everything in Insight safely
                        rec_part = "Please review the comprehensive insight above to determine your next strategic step."
                        
                    st.subheader("📌 Key Insight")
                    st.markdown(insight_part)
                    
                    st.subheader("💡 Recommendation")
                    st.markdown(rec_part)

if __name__ == "__main__":
    main()
