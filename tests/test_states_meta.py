from unittest import TestCase

from mx.states_meta import STATES


class TestStatesMeta(TestCase):

    def setUp(self) -> None:
        self.states_list = STATES

    def test_states_len(self) -> None:
        self.assertEqual(len(self.states_list), 32)

    def test_states_attr(self) -> None:
        pass
g