import streamlit as st
import time
import random
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import IsolationForest

# --- AI CORE ENGINE ---
class AIStreamingMuleEngine:
    def __init__(self):
        # Unsupervised Isolation Forest Engine for High-Dimensional Anomaly Detection
        # Contamination matches expected fraud/mule ratios in a production ledger (~10%)
        self.ai_model = IsolationForest(contamination=0.10, random_state=42)
        self.is_model_trained = False
        self.training_data_pool = []
        
        # Warm up the engine with synthetic historical baseline profiles (Normal human behavior)
        self._bootstrap_baseline_behavior()

    def _bootstrap_baseline_behavior(self):
        """Generates 150 normal banking events to train the baseline AI model"""
        for _ in range(150):
            inter_arrival = random.uniform(5000, 20000)      # High delay (Normal human speed)
            amount = random.uniform(500, 12000)             # Moderate everyday transfers
            keystroke_var = random.uniform(8.0, 22.0)        # Natural, shifting typing cadence
            device_velocity = random.choice([1, 1, 1, 2])    # Single device accessing 1 or 2 accounts max
            
            self.training_data_pool.append([inter_arrival, amount, keystroke_var, device_velocity])
        
        # Train our model on what normal customer usage profiles look like
        self.ai_model.fit(self.training_data_pool)
        self.is_model_trained = True

    def evaluate_ai_risk(self, inter_arrival, amount, keystroke_var, device_velocity):
        """
        Uses the trained Isolation Forest to compute an outlier risk index.
        Returns a scaled risk percentage (0-100%) based on isolation scores.
        """
        feature_vector = np.array([[inter_arrival, amount, keystroke_var, device_velocity]])
        
        # decision_function outputs values: negative for anomalies, positive for normal
        raw_anomaly_score = self.ai_model.decision_function(feature_vector)[0]
        
        # Transform the raw statistical distance into a human-readable risk metric
        scaled_risk = int((1.0 - (raw_anomaly_score + 0.5) / 1.0) * 100)
        return max(0, min(scaled_risk, 100))

# --- UI STYLING & CORE DASHBOARD ---
st.set_page_config(page_title="AI-Enhanced Anti-Mule Platform", layout="wide")

st.title("🧠 Intelligence-Driven Cross-Channel Anti-Mule Platform")
st.subheader("IIT Hyderabad Research Prototype — Unsupervised ML Stream Execution Engine")
st.markdown("---")

# Persistent memory state management
if "ai_engine" not in st.session_state:
    st.session_state.ai_engine = AIStreamingMuleEngine()
if "last_seen_ts" not in st.session_state:
    st.session_state.last_seen_ts = {}
if "device_counts" not in st.session_state:
    st.session_state.device_counts = {}
if "ui_logs" not in st.session_state:
    st.session_state.ui_logs = pd.DataFrame(columns=[
        "Timestamp", "Transaction ID", "Source Profile", "Destination Hub", "Amount", "AI Feature Profile", "AI Outlier Risk Status", "Mitigation Execution"
    ])

# Top Performance KPI Dashboard Panel
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    total_tx_slot = st.empty()
with kpi2:
    intercept_slot = st.empty()
with kpi3:
    ai_status_slot = st.empty()

col_left, col_right = st.columns([1, 2])

with col_left:
    st.header("Pipeline Controls")
    target_mule_acc = st.text_input("Target Sub-Graph Hub Node", "BOI_9988221100")
    attacker_hardware = st.text_input("Simulated Attack Device IMEI", "IMEI_8893012294011")
    stream_delay = st.slider("Dynamic Ingestion Interval Delay", 0.1, 2.0, 0.5)
    
    run_pipeline = st.button("▶️ Launch AI Ingestion Pipeline", type="primary")
    if st.button("🔄 Clear System State Models"):
        for key in ["last_seen_ts", "device_counts"]:
            st.session_state[key] = {}
        st.session_state.ui_logs = pd.DataFrame(columns=[
            "Timestamp", "Transaction ID", "Source Profile", "Destination Hub", "Amount", "AI Feature Profile", "AI Outlier Risk Status", "Mitigation Execution"
        ])
        st.rerun()

with col_right:
    st.header("📡 Real-Time AI Stream Ingestion Console")
    live_table_slot = st.empty()

# --- LIVE MACHINE LEARNING PIPELINE EXECUTION ---
if run_pipeline:
    victim_pool = [f"VICTIM_ACCOUNT_00{i}" for i in range(1, 6)]
    current_ms_clock = int(time.time() * 1000)
    
    for cycle in range(15):
        is_fraud_burst = cycle >= 4  # Induce coordinated script burst behaviors after cycle 4
        
        if is_fraud_burst:
            source = random.choice(victim_pool)
            dest = target_mule_acc
            amount = float(random.randint(35000, 49500))
            # Rapid script velocity (sub-second bursts)
            inter_arrival_delta = random.randint(100, 600)
            keystroke_variance = random.uniform(0.2, 1.8)     # Highly uniform typing profile (Bot/Macro signature)
            imei = attacker_hardware
        else:
            source = f"ORGANIC_RETAIL_{random.randint(100,999)}"
            dest = f"BOI_ACCOUNT_{random.randint(2000,2500)}"
            amount = float(random.randint(1200, 9500))
            # Standard human timing patterns
            inter_arrival_delta = random.randint(4500, 18000)
            keystroke_variance = random.uniform(9.5, 24.0)    # Natural human physical variability
            imei = f"IMEI_CLEAN_{random.randint(10000,99999)}"
            
        current_ms_clock += inter_arrival_delta
        
        # Calculate cross-channel account multiplexing signature
        if imei not in st.session_state.device_counts:
            st.session_state.device_counts[imei] = set()
        st.session_state.device_counts[imei].add(source)
        active_hardware_collisions = len(st.session_state.device_counts[imei])

        # Evaluate vector through our live trained Isolation Forest Machine Learning model
        ai_computed_risk = st.session_state.ai_engine.evaluate_ai_risk(
            inter_arrival=inter_arrival_delta,
            amount=amount,
            keystroke_var=keystroke_variance,
            device_velocity=active_hardware_collisions
        )

        # Map dynamic multi-tier structural response actions based on AI inference output
        if ai_computed_risk >= 70:
            action = "🚫 INTERCEPT: TRANSACTION BLOCKED & LIEN ENFORCED"
            alert_style = "OUTLIER_CRITICAL"
        elif ai_computed_risk >= 40:
            action = "⚠️ STEP-UP: MANDATORY LIVE VIDEO-KYC TRIGGERED"
            alert_style = "OUTLIER_WARNING"
        else:
            action = "✅ ALLOW: FUNDS ROUTED NATIVELY"
            alert_style = "NOMINAL_CLEAN"

        # Push calculated records directly into UI structural table frames
        new_row = {
            "Timestamp": datetime.fromtimestamp(current_ms_clock/1000).strftime('%H:%M:%S.%f')[:-3],
            "Transaction ID": f"TXN_ML_2026_{5000+cycle}",
            "Source Profile": source,
            "Destination Hub": dest,
            "Amount": f"₹{amount:,.2f}",
            "AI Feature Profile": f"Δt={inter_arrival_delta}ms, KeyVar={keystroke_variance:.2f}, HardwareOverlap={active_hardware_collisions}",
            "AI Outlier Risk Status": f"{ai_computed_risk}%",
            "Mitigation Execution": action
        }
        
        st.session_state.ui_logs = pd.concat([pd.DataFrame([new_row]), st.session_state.ui_logs], ignore_index=True)
        logs_view = st.session_state.ui_logs
        
        # Update systemic metrics layouts
        total_tx_slot.metric(label="Total Analyzed Stream Payloads", value=len(logs_view))
        intercept_slot.metric(label="AI Real-Time Holds Confirmed", value=len(logs_view[logs_view["Mitigation Execution"].str.contains("🚫")]))
        
        if alert_style == "OUTLIER_CRITICAL":
            ai_status_slot.error("🚨 CRITICAL STRUCTURAL FRAUD VECTOR DETECTED")
        elif alert_style == "OUTLIER_WARNING":
            ai_status_slot.warning("⚠️ BEHAVIORAL DEVIATION DETECTED")
        else:
            ai_status_slot.success("🟢 STREAM EVALUATION MODEL NOMINAL")

        # Display the live updating table with background-color coding based on AI alerts
        live_table_slot.dataframe(logs_view.style.map(
            lambda val: 'background-color: #ffebe6; color: #b71c1c; font-weight: bold;' if "🚫" in str(val) else (
                        'background-color: #fff3e0; color: #e65100;' if "⚠️" in str(val) else ''),
            subset=["Mitigation Execution"]
        ), use_container_width=True)
        
        time.sleep(stream_delay)