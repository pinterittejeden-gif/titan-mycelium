import time
import random

class MyceliumSensorArray:
    def __init__(self, strain_id):
        self.strain_id = strain_id
        self.baseline_voltage = 0.12  # Baseline cell potential
        
    def read_hyphal_activity(self):
        """Simulates bio-electric readouts from the PO-X1 matrix."""
        noise = random.uniform(-0.02, 0.02)
        current_voltage = self.baseline_voltage + noise
        
        # Randomly trigger a simulated pest contact event
        if random.random() > 0.85:
            current_voltage += random.uniform(0.4, 0.7)
            
        return round(current_voltage, 4)

    def verify_enzyme_payload(self, voltage):
        """Verifies high-density cocktail secretion thresholds."""
        if voltage > 0.3:
            return round(random.uniform(15.2, 22.8), 2)
        return round(random.uniform(0.1, 0.5), 2)

    def run_telemetry_loop(self):
        print(f"--- PARALLEL TELEMETRY STREAM: {self.strain_id} ---")
        print("Checking sensory-overhaul circuits and self-healing response...\n")
        
        for step in range(1, 6):
            v_read = self.read_hyphal_activity()
            enzymes = self.verify_enzyme_payload(v_read)
            system_status = "NOMINAL // HUNTING_MODE"
            
            if v_read > 0.3:
                system_status = "⚠️ INTENTIONAL INTENSE SEPARATION - TARGET ACQUIRED"
                
            print(f"[CYCLE {step}] Matrix: {v_read}V | Output: {enzymes}u/cm² | {system_status}")
            time.sleep(1)
            
        print("\n[COMPLETE] Grid verification successful. All nodes report green status.")

if __name__ == "__main__":
    monitor = MyceliumSensorArray(strain_id="PO-X1")
    monitor.run_telemetry_loop()
