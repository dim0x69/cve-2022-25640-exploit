"""
Basic TLS client. A ciphersuite may be commanded via a first argument.
Default protocol version is TLS 1.3.
"""

from scapy.config import conf
from scapy.layers.tls.session import dump_nss_keys
from automaton_cli import TLSClientAutomaton


conf.tls_nss_filename = './keylog'
conf.dump_nss_keys = True

t = TLSClientAutomaton(server='127.0.0.1', dport=11111,
                       version='tls13',
                       psk_mode="psk_dhe_ke",
                       curve='secp256r1',
                       debug=1)
t.run()
