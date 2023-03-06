@PRC
Feature: Testing User Module

   Background: common steps
    Given user is on login page
     When  User enters valid credentials
     And   Clicks login
      When user should navigate to PRC.News dashboard
    And Open Account dropdown

@tags1
      Scenario: Manage Billing
        Then Tap on manage billing
        And Add new payment method
        And Add card name
        And Add card number
        And Add expiration date
        And Add cvc
        And Tap on Add card button
        And See the add card success msg

@tags2
     Scenario: Make card as default
        Then Tap on manage billing
        Then set as default
        Then click on submit
        And  See the default success msg

@tags3
     Scenario: delete card
        Then Tap on manage billing
        Then click on delete icon
        Then clicks on delete button
        And See the card delete success msg

@tags4
     Scenario: Download invoice
        And Tap on manage billing
        And Tap on Invoice
