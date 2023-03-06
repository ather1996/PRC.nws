

Feature: Testing support us form

  Scenario: User should navigate to the support us page
    Given user is on support us page
    Then Enter First name
    Then Enter Last name
    Then Enter email address
    Then Enter Phone no.
    Then Enter company name
    Then Enter your message
    And Tap on submit button
    And user should navigate to the Thank you page



