class GymMembership:
    def __init__(self, membership_plans, additional_features, premium_features):
        self.membership_plans = membership_plans
        self.additional_features = additional_features
        self.premium_features = premium_features
        self.all_features = {**additional_features, **premium_features}
        self.members_count = 0
        self.selected_plan = None
        self.selected_features = []
        self.total_cost = 0

    # Function to display membership plans
    def display_membership_plans(self):
        print("Available Membership Plans:")
        for plan, cost in self.membership_plans.items():
            print(f"{plan}: ${cost}")
        print()

    # Function to select a membership plan
    def select_membership_plan(self):
        self.display_membership_plans()
        plan = input("Select a membership plan: ").strip()
        if plan in self.membership_plans:
            self.selected_plan = plan
            print(f"Selected plan: {self.selected_plan}\n")
        else:
            print("Invalid membership plan. Please select again.\n")
            self.select_membership_plan()

    # Function to display additional features
    def display_additional_features(self):
        print("Available Additional Features:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")
        print("\nAvailable Premium Features:")
        for feature, cost in self.premium_features.items():
            print(f"{feature}: ${cost}")
        print()

    # Function to select additional features
    def select_additional_features(self):
        self.display_additional_features()
        while True:
            feature = input(
                "Select an additional or premium feature (or 'done' to finish): "
            ).strip()
            if feature.lower() == "done":
                break
            elif feature in self.all_features:
                self.selected_features.append(feature)
                print(f"Added feature: {feature}\n")
            else:
                print("Invalid feature. Please select again.\n")

    # Function to calculate the total cost
    def calculate_cost(self):
        base_cost = self.membership_plans.get(self.selected_plan, 0)
        features_cost = sum(self.all_features.get(f, 0) for f in self.selected_features)
        self.total_cost = base_cost + features_cost
        return self.total_cost

    # Function to apply group discount
    def apply_group_discount(self):
        if self.members_count > 1:
            discount = 0.10 * self.total_cost
            self.total_cost -= discount
            print(f"Group discount applied: ${discount}\n")

    # Function to apply special offer discounts
    def apply_special_offer_discount(self):
        if self.total_cost > 400:
            self.total_cost -= 50
            print("Special offer discount of $50 applied.\n")
        elif self.total_cost > 200:
            self.total_cost -= 20
            print("Special offer discount of $20 applied.\n")

    # Function to apply premium feature surcharge
    def apply_premium_feature_surcharge(self):
        premium_selected = any(
            f in self.premium_features for f in self.selected_features
        )
        if premium_selected:
            surcharge = 0.15 * self.total_cost
            self.total_cost += surcharge
            print(f"Premium feature surcharge applied: ${surcharge}\n")

    def confirm_membership(self):
        print("Selected Membership Plan and Features:")
        print(f"Plan: {self.selected_plan}")
        print("Features:", ", ".join(self.selected_features))
        final_cost = self.total_cost * self.members_count
        print(f"Total Cost: ${final_cost}")
        confirmation = input("Confirm membership (yes/no): ").strip().lower()
        if confirmation == "yes":
            print("Membership confirmed!\n")
            return final_cost
        else:
            print("Membership canceled.\n")
            return -1

    def run(self):
        self.select_membership_plan()
        self.select_additional_features()
        self.calculate_cost()
        self.members_count = int(input("Enter the number of members signing up together: "))
        self.apply_group_discount()
        self.apply_special_offer_discount()
        self.apply_premium_feature_surcharge()
        return self.confirm_membership()
