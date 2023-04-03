import unittest

from lib.matcher import Matcher


class MatcherTestCase(unittest.TestCase):
    def test_prefixes(self):
        projects = ['front']
        services = ['prod_front']
        matcher = Matcher()

        matcher.match(projects, services)
        self.assertEqual([], matcher.get_new_projects())
        self.assertEqual({'front': ['prod_front']}, matcher.get_binds())

    def test_no_prefixes(self):
        projects = ['front']
        services = ['front']
        matcher = Matcher()

        matcher.match(projects, services)
        self.assertEqual([], matcher.get_new_projects())
        self.assertEqual({'front': ['front']}, matcher.get_binds())

    def test_new_project(self):
        projects = []
        services = ['front']
        matcher = Matcher()

        matcher.match(projects, services)
        print(matcher.get_binds())
        self.assertEqual(['front'], matcher.get_new_projects())
        self.assertEqual({'front': ['front']}, matcher.get_binds())


if __name__ == '__main__':
    unittest.main()
