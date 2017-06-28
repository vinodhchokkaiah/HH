class Test3():

    def setUp(self):
        """ Called before each test
        This method is called before each test. This is a good place to ensure
        the environment is in a known good state before starting the test.
        """
        restart()

    def test_scenario_3(self):
        """
        @summary: 
        @contact: test_author
        @tag: Testing
        @dep: 
        @req: PRD-3337: CO2 filter-line should has maximum thickness of 1cm

        Assumptions:

        Test_Design

        Initial_Setup

        Test_Procedure
