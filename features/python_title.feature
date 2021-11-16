Feature: Python title
@pyweb
  Scenario: python web title is correct
    Given chrome is up
    When user gets page
    Then the title is correct

