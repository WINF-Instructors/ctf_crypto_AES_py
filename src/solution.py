from hashlib import sha256
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

key = 78692332970999186838166635325028512999528413395648075543401505779229109996109
iv = 0xe99797bb11336fda9c58f58cffa96eea
enc_flag = 0xfeba0c8b2a091086ef02cf74957588a4987b7084312772aa6f1293c0c4f4ab41b8ac915fe0fb4bb85861eb0ca7520f9b

key2 = 9365470573153930203526300342161738390755957262423488081786729359361407398861
iv2 = 0xca46dba1351477f2766ea4ca7e64ec5b
enc_flag2 = 0x3263d244bbefdb36afa56e8b984a9e23d03d29e088648a4e3e20fc18f39abab179bc7f91848fef7f381e443fb4ca6cb8

def decrypt_flag(key, iv, enc_flag):
    key = sha256(str(key).encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, long_to_bytes(iv))
    enc_flag = long_to_bytes(enc_flag)
    return unpad(cipher.decrypt(enc_flag), 16)

    

print(decrypt_flag(key, iv, enc_flag))