from data.default import MEMBERSHIP_PLANS, ADDITIONAL_FEATURES, PREMIUM_FEATURES
from gym_membership import GymMembership


def main():
    gym_membership = GymMembership(
        MEMBERSHIP_PLANS, ADDITIONAL_FEATURES, PREMIUM_FEATURES
    )
    cost = gym_membership.run()
    print(f"Final Cost: ${cost}")


if __name__ == "__main__":
    main()
