import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.serch_repo("become-qa-auto")
    assert r["total_count"] == 58
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.serch_repo("sergiybutenco_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_be_found(github_api):
    r = github_api.serch_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_emojis_can_be_retrieved(github_api):
    r = github_api.get_emojis()
    assert "smile" in r


@pytest.mark.api
def test_commits_can_be_listed(github_api):
    r = github_api.list_commits("octocat", "Hello-World")
    assert isinstance(r, list)
    assert len(r) > 0
    assert "commit" in r[0]


@pytest.mark.api
def test_user_not_found(github_api):
    r = github_api.get_user("nonexistentuser1234567890")
    assert r.get("message") == "Not Found"


@pytest.mark.api
def test_specific_emoji_exists(github_api):
    r = github_api.get_emojis()
    assert "thumbsup" in r


@pytest.mark.api
def test_commits_for_nonexistent_repo(github_api):
    r = github_api.list_commits("octocat", "nonexistentrepo1234567890")
    assert r.get("message") == "Not Found"
