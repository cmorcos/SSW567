import unittest  # for writing unit tests

from unittest.mock import patch, Mock  # for creating mock objects and replacing functions

from github_api import get_repos, get_commit_count  # import functions to test


class TestGitHubApi(unittest.TestCase): # test class
    @patch("github_api.requests.get")   # replace requests.get() with a mock version during testing
    def test_get_repos(self, mock_get):
        mock_response = Mock()  # create mock github response
        mock_response.status_code = 200 # mock successful github response
        mock_response.json.return_value = [ # mocks 2 repos returned
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get.return_value = mock_response   # requests.get returns mock response

        result = get_repos("testuser")  # test function
        self.assertEqual(len(result), 2)    # check for 2 repos
        self.assertEqual(result[0]["name"], "repo1")    # check name of 1st repo
        self.assertEqual(result[1]["name"], "repo2")    # check name of 2nd repo

    @patch("github_api.requests.get")   # comments would be almost identical compared to code block above
    def test_get_commit_count(self, mock_get):
        mock_response = Mock()  
        mock_response.status_code = 200
        mock_response.json.return_value = [ # 3 commits rather than 2 repos
            {"commit": "1"},
            {"commit": "2"},
            {"commit": "3"}
        ]
        mock_get.return_value = mock_response

        result = get_commit_count("testuser", "repo1")
        self.assertEqual(result, 3) # check for 3 commits rather than 2 repos

    @patch("github_api.requests.get")   # test for when github returns error
    def test_get_repos_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404 # common 404 not found error
        mock_get.return_value = mock_response
        result = get_repos("fakeuser")  # for get_repos function
        self.assertEqual(result, [])    # should be empty list


if __name__ == "__main__":
    unittest.main()