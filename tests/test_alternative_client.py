import unittest
from alternative_lib import alternative_client
from .test_data import TEST_DATASETS


test_client = alternative_client.AlternativeClient(
    site_url='http://dev.localhost:5000'
)


class TestGetDatasets(unittest.TestCase):

    def test_get_datasets_no_metadata(self):
        # All datasets
        results = test_client.get_datasets(
            datasets=TEST_DATASETS
        )
        self.assertEqual(len(results), 4)

    def test_get_datasets_metadata_field(self):
        # Datasets with author -> test1
        metadata = {
            'author': 'test1'
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 1)

        # Datasets with author -> test1 or test2
        metadata = {
            'author': ['test1', 'test2']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 2)

        # Datasets with author -> test2
        # and maintainer -> test3 or test4
        metadata = {
            'author': 'test2',
            'maintainer': ['test3', 'test4']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 1)

    def test_get_datasets_metadata_extra_fields(self):
        # Datasets with extra field extra-field-1 with value -> test1
        metadata = {
            'extras': [{'key': 'extra-field-1', 'value': 'test1'}]
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 1)

        # Datasets with extra field extra-field-2 with value -> test2 or test4
        metadata = {
            'extras': [{'key': 'extra-field-2', 'value': ['test2', 'test4']}]
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 2)

        # Datasets with extra field extra-field-1 with value -> test1 or test3
        # and with extra field extra-field-2 with value -> test4
        metadata = {
            'extras': [
                {'key': 'extra-field-1', 'value': ['test1', 'test3']},
                {'key': 'extra-field-2', 'value': 'test4'}
            ]
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 1)

    def test_get_datasets_in_groups(self):
        # Datasets in group -> test-group-2
        metadata = {
            'groups': ['test-group-2']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 2)

        # Datasets in group -> test-group-1 and test-group-2
        metadata = {
            'groups': ['test-group-1', 'test-group-2']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 1)

        # Datasets in group -> test-group-1 or test-group-2
        metadata = {
            'groups': ['test-group-1', 'test-group-2']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata,
            not_all_groups=True
        )
        self.assertEqual(len(results), 3)

    def test_get_datasets_with_tags(self):
        # Datasets with tag -> tag1
        metadata = {
            'tags': ['tag1']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 2)

        # Datasets with tag -> tag1 and tag2
        metadata = {
            'tags': ['tag1', 'tag2']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 1)

        # Datasets with tag -> tag1 or tag2
        metadata = {
            'tags': ['tag1', 'tag2']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata,
            not_all_tags=True
        )
        self.assertEqual(len(results), 3)

    def test_get_datasets_in_organization(self):
        # Datasets in organization -> test-org-1
        metadata = {
            'organization': 'test-org-1'
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 1)

        # Datasets in organization -> test-org-1 or test-org-2
        metadata = {
            'organization': ['test-org-1', 'test-org-2']
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 2)

    def test_get_datasets_more_metadata(self):
        # Datasets with author -> test1
        # maintainer -> test4
        # in organization -> test-org-1
        # in group -> test-group-1
        # with tag -> tag1
        # with extra field extra-field-1 with value -> test1
        metadata = {
            "author": "test1",
            "maintainer": "test4",
            "organization": "test-org-1",
            "groups": ["test-group-1"],
            "tags": ["tag1"],
            "extras": [{"key": "extra-field-1", "value": "test1"}]
        }
        results = test_client.get_datasets(
            datasets=TEST_DATASETS,
            metadata=metadata
        )
        self.assertEqual(len(results), 1)
