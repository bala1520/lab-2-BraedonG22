'''
Test cases for the right_arrow module.
'''
import right_arrow as right_arrow

class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["*", "#"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        right_arrow.right_arrow()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')

        assert all(x in all_outputs for x in ['      #','******##','******###']), "Make sure that the number is not printed"

    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["-", "*"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        right_arrow.right_arrow()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')
        assert all(x in all_outputs for x in ['      *','------**','------***']), "Make sure that the number is not printed"
