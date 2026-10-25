from app import analyze_message

def test_never_sends_email(): assert analyze_message('Please follow up by Friday')['sent'] is False
