# 🛡️ Cross-Channel Financial Intelligence & Real-Time Mule Account Mitigation
> **An AI-Powered Streaming Engine for Unsupervised Outlier Detection and Transaction Interception.**
> *Developed for the Bank of India x IIT Hyderabad National Innovation Framework Hackathon (Problem Statement #BOI-IITH-2026)*

---

## 🚀 Live Environment Runtimes
- **🌐 Interactive Simulation Dashboard:**(https://boi-iith-anti-mule-engine-qwjwzkxkhfs9tq7noe7cat.streamlit.app/)
- **💻 Open-Source Code Core:** https://github.com/Ritesh12911/boi-iith-anti-mule-engine

---

## 💡 The Core Innovation Paradigm

Legacy Anti-Money Laundering (AML) and Fraud Monitoring Systems fail in active production because of two architectural constraints: the **Latency Trap** (relying on static database snapshots compiled hours after the transaction) and the **Cross-Bank Blind Spot** (treating data within individual institutional silos). Coordinated cyber-fraud syndicates exploit this by using automated script macros to cascade stolen funds across multiple layer accounts across separate banks within seconds.

This framework introduces a real-time, event-driven optimization layer that shifts defenses from *reactive investigation* to *in-flight stream interception*.

### 🧠 Advanced AI Architecture Pillars

1. **Continuous Temporal Evaluation (TGN Intuition):** Treats the transactional ecosystem as a continuous-time dimension rather than static row snapshots. The engine computes inter-arrival velocity deltas ($\Delta t$) at a millisecond scale directly inside the ingestion queue.
2. **Unsupervised High-Dimensional Machine Learning:** Deploys a live-trained **Isolation Forest Anomaly Detection Model**. By mapping transactions across an array of independent behavioral vectors simultaneously, the model self-bootstraps and flags structural outlier signatures without relying on static, hardcoded thresholds or outdated historical labels.
3. **Zero-Trust Device & Biometric Telemetry:** Evaluates behavioral typing cadence variables (keystroke flight variations) alongside multi-account hardware token collisions. This instantly exposes automated bots, macro execution scripts, or localized fraud rings managing dozens of rented/compromised customer profiles from a single control point.

---

## 🏗️ System Flow & Data Pipeline Architecture
[ Real-Time Channels ] ──> ( Kafka Event Bus ) ──> [ Flink State Processor ]
(UPI/IMPS/ATM)                                              │
▼
[ Action: Active Intercept ] <── ( Edge Interceptor ) <── [ ML Inference Engine ]

Hard Debit Liens              - 75%+ Outlier Score     - Isolation Forest

Step-Up Video KYC            - Automated Routing API   - Biometric/Network Vectors

## 📊 High-Dimensional Enterprise Feature Schema

The engine feeds streaming data matrices into the unsupervised model core across four data pillars:

| Evaluation Vector | Explicit Data Fields Ingested | Downstream Machine Learning Utility |
| :--- | :--- | :--- |
| **Temporal Stream Logs** | `Timestamp_Epoch (ms)`, `Inter_Arrival_Delta ($\Delta t$)`, `Flow_Direction_Ratio` | Quantifies spatial and temporal transaction velocity to identify structural cascading trends. |
| **Interaction Biometrics** | `Keystroke_Dwell_Time`, `Swipe_Path_Vector`, `Device_Cadence_Variance` | Differentiates manual, organic human application access from uniform automated bot injections. |
| **Hardware Fingerprinting**| `Device_IMEI`, `IP_Routing_Subnet`, `Active_Account_Multiplex_Count` | Maps hardware token footprint collisions across seemingly unlinked retail profiles. |
| **External Intel Feeds** | `NCCRP_Cyber_Ticket_No`, `I4C_Threat_Weight`, `Flagged_IFSC_Nodes` | Establishes immediate deterministic seed vectors to isolate associated network sub-graphs. |

---

## 🛠️ Technology Stack Specifications

- **Stateful Ingestion Compute Fabric:** `Apache Kafka` & `Apache Flink` concepts for low-latency streaming window state extraction.
- **Machine Learning Core Engine:** `scikit-learn` handling unsupervised multivariate Isolation Forest modeling.
- **Vector Compute & Serialization:** `NumPy` & `Pandas` for real-time high-speed feature coordinate translations.
- **Visual Validation Interface:** `Streamlit Community Cloud` pipeline infrastructure.

---

## ⚙️ Local Development Deployment Framework

To test the machine learning streaming simulation model on a local workstation environment, execute the setup framework sequentially:

```bash
# Clone the enterprise repository
git clone [https://github.com/Ritesh12911/boi-iith-anti-mule-engine.git](https://github.com/Ritesh12911/boi-iith-anti-mule-engine.git)
cd boi-iith-anti-mule-engine

# Initialize standard requirements dependencies
pip install -r requirements.txt

# Launch the reactive local server dashboard runtime
python -m streamlit run app1.py
