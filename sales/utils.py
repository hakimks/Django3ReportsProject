import uuid
def generate_code():
    code = uuid.uuid4()
    code_mod = str(code).replace('-','').upper()[:12]
    return code_mod