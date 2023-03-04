Feature: Orders
"""
Confirm that we can browse the orders related pages on our site
"""

Scenario: success for visiting orders and orders details pages
    Given I navigate to the orders pages
    When I click on the link to order details
    Then I should see the order details for that Order