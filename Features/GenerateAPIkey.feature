@PRC
Feature: Testing User Module

   Background: common steps
    Given user is on login page
     When  User enters valid credentials
     And   Clicks login

@tags1
     Scenario: Generate New API Key.
       Then Tap on Generate API key button
       And clicks on Generate New API key
       Then Enter Name
       Then Enter Description
       Then clicks on submit button
       And See the success message

@tags2
     Scenario: user will able to Delete the API
       Then Tap on Generate API key button
       And open delete popup
       Then click on delete button
       And See the delete msg

@tags3
     Scenario: user will able to view the full API
       Then Tap on Generate API key button
       And click on eye icon

@tags4
     Scenario: User can easily copy the API Key
        Then   Tap on Generate API key button
        And  Tap on Copy icon
        And See the copy success msg


