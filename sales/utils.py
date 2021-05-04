import uuid
def generate_code():
    code = uuid.uuid4()
    code_mod = str(code).replace('-','')[:12]
    return code_mod