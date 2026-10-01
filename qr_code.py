import qrcode

# vCard 3.0 avec réseaux sociaux intégrés (URL/NOTE)
vcard_data = """BEGIN:VCARD
VERSION:3.0
N:Choura;Fares;;;
FN:Fares Choura
TEL;TYPE=CELL,VOICE:+21627859001
TEL;TYPE=WHATSAPP:+21627859001
EMAIL:fareschoura8@gmail.com
ADR;TYPE=HOME:;;5 Rue Bayrouni;Soukra;Ariana;;Tunisie
URL;TYPE=Instagram:https://instagram.com/fares_choura
URL;TYPE=Facebook:https://facebook.com/FaresChoura
NOTE:Propriétaire de Dax (Chat Siamois) | Insta: @fares_choura | FB: Fares Choura
END:VCARD"""

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=2,
)

qr.add_data(vcard_data)
qr.make(fit=True)

# Génération avec les couleurs inspirées du Siamois (Seal Point)
# Fond beige crème / Motif brun foncé chocolat
img = qr.make_image(fill_color="#2B1B17", back_color="#FDFBF7")
img.save("dax_vcard_styled.png")

print("QR Code vCard généré !")