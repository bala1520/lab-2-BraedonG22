'''
Test cases for the telephone module.
'''
import telephone as telephone

class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["8005551212"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        telephone.telephone()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')

        assert "(800) 555-1212" in all_outputs, "Make sure that the number is formatted correctly"

    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["9995551111"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        telephone.telephone()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')
        assert "(999) 555-1111" in all_outputs, "Make sure that the number is formatted correctly"
