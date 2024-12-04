from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def create_keys(user_id):
    private_key = rsa.generate_private_key(
         public_exponent=65537,
         key_size=2048,
    )

    public_key = private_key.public_key()

    with open(f"Keys_{user_id}/public_key.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )
    with open(f"Keys_{user_id}/private_key.pem", "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

create_keys(1)
create_keys(2)
