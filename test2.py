class Test2():

    def setUp(self):
        """ Called before each test
        This method is called before each test. This is a good place to ensure
        the environment is in a known good state before starting the test.
        """
        restart()

    def test_scenario_2(self):
        """
        @summary: 
        @contact: test_author
        @tag: Testing
        @dep: 
        @req: SRD-NIBP-3336: NIBP hose should have a minimum of 100cm length

        Assumptions:

        Test_Design

        Initial_Setup

        Test_Procedure
