import uuid
def generate_code():
    code = uuid.uuid4()
    code_mod = str(code).replace('-','')
    return code_mod