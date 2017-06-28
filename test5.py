class Test5():

    def setUp(self):
        """ Called before each test
        This method is called before each test. This is a good place to ensure
        the environment is in a known good state before starting the test.
        """
        restart()

    def test_scenario_5(self):
        """
        @summary: 
        @contact: test_author
        @tag: Testing
        @dep: 
        @req: PRD-3339: Temperature can read from maximum of 3 channels from patient body.

        Assumptions:

        Test_Design

        Initial_Setup

        Test_Procedure
