import unittest

from lib.matcher import Matcher


class MatcherTestCase(unittest.TestCase):
    def test_new_project(self):
        projects = []
        services = ['front']
        matcher = Matcher()

        matcher.match(projects, services)
        print(matcher.get_binds())
        self.assertEqual(['front'], matcher.get_new_projects())
        self.assertEqual({'front': ['front']}, matcher.get_binds())

    def test_new_projects_wuth_prefixes(self):
        projects = []
        services = ['prod_front', 'test_back']
        matcher = Matcher()

        matcher.match(projects, services)
        print(matcher.get_binds())
        self.assertEqual(['front', 'back'], matcher.get_new_projects())
        expected_binds = {
            'front': ['prod_front'],
            'back': ['test_back']
        }
        self.assertEqual(expected_binds, matcher.get_binds())

    def test_no_prefixes_wo_new_project(self):
        projects = ['front']
        services = ['front']
        matcher = Matcher()

        matcher.match(projects, services)
        self.assertEqual([], matcher.get_new_projects())
        self.assertEqual({'front': ['front']}, matcher.get_binds())

    def test_prefixes_wo_new_project(self):
        projects = ['front']
        services = ['prod_front']
        matcher = Matcher()

        matcher.match(projects, services)
        self.assertEqual([], matcher.get_new_projects())
        self.assertEqual({'front': ['prod_front']}, matcher.get_binds())

    def test_prefixes_two_projects(self):
        projects = ['front', 'back']
        services = ['prod_front', 'test_front', 'prod_back', 'test_back']
        matcher = Matcher()

        matcher.match(projects, services)
        self.assertEqual([], matcher.get_new_projects())
        expected_binds = {
            'front': ['prod_front', 'test_front'],
            'back': ['prod_back', 'test_back']
        }
        self.assertEqual(expected_binds, matcher.get_binds())

    def test_suffixes_wo_new_project(self):
        projects = ['front']
        services = ['front_az1']
        matcher = Matcher()

        matcher.match(projects, services)
        self.assertEqual([], matcher.get_new_projects())
        self.assertEqual({'front': ['front_az1']}, matcher.get_binds())

    def test_prefixes_and_suffixes_wo_new_project(self):
        projects = ['front']
        services = ['prod_front_az1']
        matcher = Matcher()

        matcher.match(projects, services)
        self.assertEqual([], matcher.get_new_projects())
        self.assertEqual({'front': ['prod_front_az1']}, matcher.get_binds())

    def test_prefixes_and_suffixes_w_new_project(self):
        projects = []
        services = ['prod_front_aaa']
        matcher = Matcher()

        matcher.match(projects, services)
        self.assertEqual(['front_aaa'], matcher.get_new_projects())
        self.assertEqual({'front_aaa': ['prod_front_aaa']}, matcher.get_binds())


if __name__ == '__main__':
    unittest.main()
