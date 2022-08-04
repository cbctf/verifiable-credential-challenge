from ecdsa import ECDH, NIST256p, SigningKey

from ..derive_ecdh import *

# Generate the same shared secret from imported generated keys
def test_ecdh_derive_shared_secret():

    # Import keys for two participating users
    holderSecretKey = "23832cbef38641b8754a35f1f79bbcbc248e09ac93b01c2eaf12474f2ac406b6"
    holderPublicKey = "04fd4ca9eb7954a03517ac8249e6070aa3112e582f596b10f0d45d757b56d5dc0395a7d207d06503a4d6ad6e2ad3a1fd8cc233c072c0dc0f32213deb712c32cbdf"

    bobSecretKey = "2d1b242281944aa58c251ce12db6df8babd703b5c0a1fc0b9a34f5b7b9ad6030"
    bobPublicKey = "04e35cde5e3761d075fc87b3b0983a179e1b8e09da242e79965d657cba48f792dfc9b446a098ab0194888cd9d53a21c873c00264275dba925c2db6c458c87ca3d6"

    # Each user derives the same shared secret, independantly, using the other's public key which is exchanged
    holderSecret = derive_shared_secret(holderSecretKey, bobPublicKey)
    print("holder secret: ", holderSecret.hex())
    bobSecret = derive_shared_secret(bobSecretKey, holderPublicKey)
    print("Bob secret: ", bobSecret.hex())

    assert holderSecret == bobSecret, "Both parties should generate the same secret"


# Generate the same shared secret from random keys
def test_ecdh_derive_shared_secret_random():

    # Generate random keys for the two participating users
    holderSecretKey = SigningKey.generate(curve=NIST256p)
    holder = ECDH(curve=NIST256p)
    holder.load_private_key(holderSecretKey)
    holderPublicKey = holder.get_public_key()

    bobSecretKey = SigningKey.generate(curve=NIST256p)
    bob = ECDH(curve=NIST256p)
    bob.load_private_key(bobSecretKey)
    bobPublicKey = bob.get_public_key()

    # Each user derives the same shared secret, independantly, using the other's public key which is exchanged
    holderSecret = derive_shared_secret_from_key(holderSecretKey, bobPublicKey)
    print("holder secret: ", holderSecret.hex())
    bobSecret = derive_shared_secret_from_key(bobSecretKey, holderPublicKey)
    print("Bob secret: ", bobSecret.hex())

    assert holderSecret == bobSecret, "Both parties should generate the same secret"


# Test the entire key generation flow, DeriveECDHSecret() into ConcatKDF()
def test_ecdh_generate_key():

    holderSecretKey = "23832cbef38641b8754a35f1f79bbcbc248e09ac93b01c2eaf12474f2ac406b6"
    holderPublicKey = "04fd4ca9eb7954a03517ac8249e6070aa3112e582f596b10f0d45d757b56d5dc0395a7d207d06503a4d6ad6e2ad3a1fd8cc233c072c0dc0f32213deb712c32cbdf"

    bobSecretKey = "2d1b242281944aa58c251ce12db6df8babd703b5c0a1fc0b9a34f5b7b9ad6030"
    bobPublicKey = "04e35cde5e3761d075fc87b3b0983a179e1b8e09da242e79965d657cba48f792dfc9b446a098ab0194888cd9d53a21c873c00264275dba925c2db6c458c87ca3d6"

    holderSecret = derive_shared_secret(holderSecretKey, bobPublicKey)
    print("holder secret: ", holderSecret.hex())
    bobSecret = derive_shared_secret(bobSecretKey, holderPublicKey)
    print("Bob secret: ", bobSecret.hex())

    # Header parameters used in ConcatKDF
    alg = "A256GCM"
    apu = "holder"
    apv = "Bob"
    keydatalen = 32  # 32 bytes or 256 bit output key length

    # After each side generates the shared secret, it is used to independantly derive a shared encryption key
    holderKey = concat_kdf(holderSecret, alg, apu, apv, keydatalen)
    print("holder key: ", holderKey.hex())

    bobKey = concat_kdf(bobSecret, alg, apu, apv, keydatalen)
    print("Bob key: ", bobKey.hex())

    assert (
        holderKey == bobKey
    ), "Both parties should generate the same key from the same secret"


# Test the entire key generation flow, derive_shared_secret() into concat_kdf()
def test_ecdh_generate_key_random():

    holderSecretKey = SigningKey.generate(curve=NIST256p)
    holder = ECDH(curve=NIST256p)
    holder.load_private_key(holderSecretKey)
    holderPublicKey = holder.get_public_key()

    bobSecretKey = SigningKey.generate(curve=NIST256p)
    bob = ECDH(curve=NIST256p)
    bob.load_private_key(bobSecretKey)
    bobPublicKey = bob.get_public_key()

    holderSecret = derive_shared_secret_from_key(holderSecretKey, bobPublicKey)
    print("holder secret: ", holderSecret.hex())
    bobSecret = derive_shared_secret_from_key(bobSecretKey, holderPublicKey)
    print("Bob secret: ", bobSecret.hex())

    # Header parameters used in ConcatKDF
    alg = "A256GCM"
    apu = "holder"
    apv = "Bob"
    keydatalen = 32  # 32 bytes or 256 bit output key length

    # After each side generates the shared secret, it is used to independantly derive a shared encryption key
    holderKey = concat_kdf(holderSecret, alg, apu, apv, keydatalen)
    print("holder key: ", holderKey.hex())

    bobKey = concat_kdf(bobSecret, alg, apu, apv, keydatalen)
    print("Bob key: ", bobKey.hex())

    assert (
        holderKey == bobKey
    ), "Both parties should generate the same key from the same secret"


def main():

    test_ecdh_derive_shared_secret()
    test_ecdh_derive_shared_secret_random()
    test_ecdh_generate_key()
    test_ecdh_generate_key_random()


if __name__ == "__main__":
    main()
    print("All tests passed")
