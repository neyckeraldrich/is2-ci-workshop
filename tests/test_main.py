import pytest
from app.gym_membership import GymMembership
from app.data.default import MEMBERSHIP_PLANS, ADDITIONAL_FEATURES, PREMIUM_FEATURES


@pytest.fixture
def gym():
    return GymMembership(MEMBERSHIP_PLANS, ADDITIONAL_FEATURES, PREMIUM_FEATURES)


def test_membership_selection(gym):
    gym.selected_plan = "Basic"
    assert gym.selected_plan == "Basic"


def test_additional_features_selection(gym):
    gym.selected_features = ["Personal Training"]
    assert "Personal Training" in gym.selected_features


def test_cost_calculation(gym):
    gym.selected_plan = "Basic"
    gym.selected_features = ["Personal Training"]
    total_cost = gym.calculate_cost()
    assert total_cost == 80


def test_group_discount(gym):
    gym.selected_plan = "Basic"
    gym.selected_features = ["Personal Training"]
    gym.calculate_cost()
    gym.members_count = 2
    gym.apply_group_discount()
    assert gym.total_cost == 72


def test_special_offer_discount(gym):
    gym.total_cost = 450
    gym.apply_special_offer_discount()
    assert gym.total_cost == 400


def test_premium_feature_surcharge(gym):
    gym.total_cost = 100
    gym.selected_features = ["Exclusive Facilities"]
    gym.apply_premium_feature_surcharge()
    assert gym.total_cost == 115


def test_invalid_input(gym):
    with pytest.raises(KeyError):
        gym.membership_plans["InvalidPlan"]


def test_membership_confirmation(gym, mocker):
    gym.selected_plan = "Basic"
    gym.selected_features = ["Personal Training"]
    gym.calculate_cost()
    gym.total_cost = 80
    gym.members_count = 1
    mocker.patch("builtins.input", return_value="yes")
    result = gym.confirm_membership()
    assert result == 80


if __name__ == "__main__":
    pytest.main()
