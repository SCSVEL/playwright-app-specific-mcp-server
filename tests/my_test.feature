@Regression
Feature: Create a customer
  In order to enable the customer
  Register the account

  Scenario: Create a new account
    Given we are in home page
    Then Click the 'new account' link
    When the 'New Account' title appears
    Then fill the fields: <First Name>, <Last Name> #etc
    Then click the Submit link
    When the 'Account Created!' title appears
    Then the account should be created successfully

    Examples:
      | First Name | Last Name | Email | Password |
      | John       | Doe       |       |          |
