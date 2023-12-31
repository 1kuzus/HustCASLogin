const window={}
require('./jsencrypt').myfunc(window)
const encrypt = new window.JSEncrypt()
encrypt.setPublicKey('MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJ7aKWURpJx4m8i4pB9P2pzNriT3UyhK6H20meKv8gFJmERA482JSi/DvZ4SkxP9INL5h8lGGvu5W3eTrpJaN3MCAwEAAQ==')

function strEnc(text)
{
    return encrypt.encrypt(text)
}