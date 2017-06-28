class Test1():

    def setUp(self):
        """ Called before each test
        This method is called before each test. This is a good place to ensure
        the environment is in a known good state before starting the test.
        """
        restart()

    def test_scenario_1(self):
        """
        @summary:
        @contact: test_author
        @tag: Testing
        @dep: 
        @req: SRD-OXI-3335: Spo2 cable should contain two ends, which connects the device at one end and sensor at other end        

        Assumptions:

        Test_Design

        Initial_Setup

        Test_Procedure
