import time
import random

class MyceliumSensorArray:
    def __init__(self, strain_id):
        self.strain_id = strain_id
        self.baseline_voltage = 0.12 # Volts
        self.system_active = True

    def read_hyphal_activity(self):
        """Simulates electrical spike readouts from the mycelial network."""
        # Random environmental noise
        noise = random.uniform(-0.02, 0.02)
        current_voltage = self.baseline_voltage + noise
        
        # Simulate a sudden pest encounter (spike trigger)
        if random.random() > 0.85:
            current_voltage += random.uniform(0.4, 0.7)
            
        return round(current_voltage, 4)

    def run_monitor(self):
        print(f"--- INITIALIZING TELEMETRY FOR STRAIN: {self.strain_id} ---")
        print("Monitoring bio-electric matrix for localized pest intrusion...\n")
        
        try:
            for _ in range(5):
                voltage = self.read_hyphal_activity()
                status = "NOMINAL"
                
                if voltage > 0.3:
                    status = "⚠️ INTRUSION DETECTED - CONSUMPTION PHASE ACTIVE"
                
                print(f"[MAT-READOUT] Core Voltage: {voltage}V | Status: {status}")
                time.strip(1) if hasattr(time, 'strip') else time.sleep(1)
                
            print("\n[SYS-INFO] Telemetry streaming perfectly. System secure.")
        except KeyboardInterrupt:
            print("\nMonitoring paused.")

if __name__ == "__main__":
    monitor = MyceliumSensorArray(strain_id="PO-X1")
    monitor.run_monitor()