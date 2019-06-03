from unittest import TestCase
from mexico.states import States


class StatesTestCase(TestCase):
    def setUp(self) -> None:
        self.states = States()

    def test_state_basics(self):
        self.assertEqual(32, self.states.num_of_states())
        self.assertEqual('Oaxaca', self.states.state_name(20))
        self.assertEqual(20, self.states.state_number('Oaxaca'))

    def test_state_data(self):
        self.assertEqual(570, self.states.oaxaca.municipality_count())
        self.assertEqual(93_757, self.states.oaxaca.territory_in_km_2)


