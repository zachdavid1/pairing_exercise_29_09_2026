from lib.script import format_participants


def test_format_participants():
    assert format_participants(["Bart"]) == "Bart"
    assert format_participants(["Bart", "Lisa"]) == "Bart & Lisa"
    assert format_participants(["Bart", "Lisa", "Maggie"]) == "Bart, Lisa & Maggie"
