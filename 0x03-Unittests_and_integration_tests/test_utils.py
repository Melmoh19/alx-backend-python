#!/usr/bin/env python3
""" test utils"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """ test different inputs """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test correct access """
        self.assertEqual(access_nested_map(nested_map, path), expected)

        @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")), ])
        def test_access_nested_map_exception(self, nested_map, path):
            """test exception raised"""
            with self.assertRaises(KeyError) as context:
                access_nested_map(nested_map, path)
            self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """ test json fetching"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """test get_json method with mock"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('utils.requests.get', return_value=mock_response) as mkget:
            result = get_json(test_url)

            mkget.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ memoize class """
    def test_memoize(self):
        """ test memoize """
        class TestClass:
            """ test class"""
            def a_method(self):
                """"class method"""
                return 42

            @memoize
            def a_property(self):
                """ property method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mck_mthd:
            test_obj = TestClass()
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mck_mthd.assert_called_once()


if __name__ == '__main__':
    unittest.main()
