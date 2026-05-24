import random

class Agent:
    """Represents an autonomous agent proposing actions."""
    def __init__(self, name):
        self.name = name

    def propose_action(self):
        """Agent proposes a new destination (x, y)."""
        # Simulate agent intelligence: sometimes it picks a good path, sometimes a potentially problematic one
        if random.random() < 0.7: # 70% chance to pick a "safe" destination
            # Example: destination far from restricted zones
            dest_x = random.randint(7, 15)
            dest_y = random.randint(7, 15)
        else: # 30% chance to pick a "risky" destination (potentially in or near a restricted zone)
            # Example: destination near a known restricted zone center (5,5)
            restricted_x_center = 5
            restricted_y_center = 5
            dest_x = random.randint(restricted_x_center - 2, restricted_x_center + 2)
            dest_y = random.randint(restricted_y_center - 2, restricted_y_center + 2)

        print(f"[{self.name}] Agent proposes moving to destination: ({dest_x}, {dest_y})")
        return (dest_x, dest_y)

class FaithfulnessGate:
    """
    A gate that checks an agent's proposed action against predefined rules
    to ensure faithfulness to objectives and constraints (e.g., safety, ethics).
    """
    def __init__(self, restricted_zones):
        # restricted_zones: List of (center_x, center_y, radius) tuples
        self.restricted_zones = restricted_zones

    def is_faithful(self, proposed_destination):
        """
        Checks if the proposed destination violates any restricted zones.
        Returns True if faithful (safe to proceed), False otherwise (action blocked).
        """
        dest_x, dest_y = proposed_destination
        for zone_x, zone_y, radius in self.restricted_zones:
            # Simple distance check: if destination is within radius of a restricted zone center
            distance_sq = (dest_x - zone_x)**2 + (dest_y - zone_y)**2
            if distance_sq <= radius**2:
                # --- ARTICLE CONCEPT ILLUSTRATION START ---
                # This is the core function of the Faithfulness Gate.
                # It intercepts the agent's proposed action and checks it against critical rules.
                print(f"  [Faithfulness Gate] ALERT: Proposed destination ({dest_x}, {dest_y}) is too close to restricted zone ({zone_x}, {zone_y}) with radius {radius}.")
                return False # Action is NOT faithful to safety rules
                # --- ARTICLE CONCEPT ILLUSTRATION END ---
        return True # Action is faithful and safe

# --- Main simulation --- 
if __name__ == "__main__":
    # Define critical constraints: areas where the agent must NOT go.
    # These are represented as (center_x, center_y, radius).
    restricted_areas = [
        (5, 5, 2),  # A restricted zone around (5,5) with radius 2 units
        (1, 8, 1)   # Another restricted zone around (1,8) with radius 1 unit
    ]

    print("--- Initializing Agent and Faithfulness Gate ---")
    delivery_agent = Agent("DeliveryBot-001")
    safety_gate = FaithfulnessGate(restricted_areas)
    print(f"Defined Restricted Zones: {restricted_areas}\n")

    print("--- Simulating Agent Decisions and Gate Checks ---")
    for i in range(5): # Simulate 5 decision cycles
        print(f"\n--- Cycle {i+1} ---")
        proposed_dest = delivery_agent.propose_action()

        if safety_gate.is_faithful(proposed_dest):
            print(f"  [Faithfulness Gate] APPROVED: Agent's action to ({proposed_dest[0]}, {proposed_dest[1]}) is faithful. Proceeding with execution.")
            # In a real system, the action (e.g., move to destination) would now be executed.
        else:
            # --- ARTICLE CONCEPT ILLUSTRATION START ---
            # This demonstrates the Faithfulness Gate actively preventing an undesirable outcome.
            # The agent's action is blocked because it violates a critical reliability constraint.
            print(f"  [Faithfulness Gate] BLOCKED: Agent's action to ({proposed_dest[0]}, {proposed_dest[1]}) is NOT faithful. Action prevented.")
            # In a real system, the agent might be prompted to re-evaluate its decision,
            # or a default safe action might be taken.
            # --- ARTICLE CONCEPT ILLUSTRATION END ---

    print("\n--- Simulation Complete ---")
