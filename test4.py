class Test4():

    def setUp(self):
        """ Called before each test
        This method is called before each test. This is a good place to ensure
        the environment is in a known good state before starting the test.
        """
        restart()

    def test_scenario_4(self):
        """
        @summary: 
        @contact: test_author
        @tag: Testing
        @dep: 
        @req: SRD-IBP-3338: There should be 5 types of IBP channels in device.

        Assumptions:

        Test_Design

        Initial_Setup

        Test_Procedure
