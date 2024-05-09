'''Script to populate the database with some initial data.
   In reality you would probably create a separate editor or a tool for importing data from elsewhere,
   but for CM1102 we'll just use this script to populate the database.'''

from app import app, db
from ListItems import Sneaker

sneakers = [
    { "name": "Jordan 1 Retro High Dark Mocha", "price": "£175", "description": "Jordan Brand continued their Black Toe design theme in 2020 and released the Jordan 1 High Dark Mocha, now available on StockZ. The Dark Mocha 1 was one of the most anticipated releases in 2020 due to its familiar colorblocking that referenced two of the greatest Jordan 1s of all-time, the Jordan 1 Travis Scott and the Jordan 1 Black Toe. The upper of the Jordan 1 High Dark Mocha features a Sail leather base with black leather surrounding the toe box and Mocha suede on the heel and ankle. A black leather Swoosh, Jordan Wings logo on the ankle, and Nike Air branding on the tongue pays homage to branding that can be found on the original 1985 Jordan 1. A Sail midsole and black outsole complete this Black Toe design. The Jordan 1 High Dark Mocha released in October of 2020.", "imageTag": "Jordan 1 Retro High Dark Mocha.png" },
    { "name": "Jordan 1 Retro High OG Spider-Man", "price": "£200", "description": "Nike and Jordan Brand are returning back to the Spider-Verse for their second Spider-Man themed Air Jordan 1, with the release of the Air Jordan 1 High OG Spider-Man Across the Spider-Verse. Also known as the Next Chapter, the Jordan 1 High OG Spider-Man Across the Spider-Verse is the next iteration of the original Air Jordan 1 Chicago colorway. The limited edition sneakers are constructed using various leathers, suedes, and other premium materials across the uppers. The patterns used across the sneakers are designed to mimic the Miles Morales/Spider-Man animation style. The Air Jordan 1 High OG Spider-Man Across the Spider-Verse released May 20, 2023.", "imageTag": "Jordan 1 Retro High OG Across the Spider Verse.png" },
    { "name": "Jordan 1 Retro High OG University Blue", "price": "£170", "description": "Jordan Brand paid homage to MJ's alma mater with the Air Jordan 1 High University Blue. The University Blue colorway is prominent in the Jordan 1's history. The first UNC-inspired Jordan 1 dates back to 1985 when the Jordan 1 debuted. Since then, there have been numerous iterations of the UNC 1, most recently the Jordan 1 Retro High Fearless UNC To Chicago. Jumpman is building off of its past and switching it up this week with a new iteration. The upper of the Air Jordan 1 High University Blue is composed of a white and black tumbled leather upper with University Blue Durabuck overlays. Following traditional Jordan 1 detailing, a Nike Air woven label is located on the tongue and an Air Jordan Wings Logo is printed on the ankle. A white midsole and University Blue outsole complete rejuvenated classic. The Air Jordan 1 High University Blue released in March of 2021", "imageTag": "Jordan 1 Retro High OG University Blue.png" },
    { "name": "Jordan 1 Retro High Court Purple White", "price": "£170", "description": "Jordan Brand added a new colorway to the silhouette that started it all with the Jordan 1 Retro High Court Purple White, now available on StockZ. This release follows similar design elements as the Chicago 1, only this time replacing red with Court Purple. This Jordan 1 consists of a white leather upper with Court Purple overlays and black detailing. A black Swoosh and Wings logo, white midsole, and Court Purple outsole completes the design. These sneakers released in April of 2020", "imageTag": "Jordan 1 Retro High Court Purple White.png" },
    { "name": "New Balance 2002R", "price": "£150", "description": "The New Balance 2002R Protection Pack Rain Cloud features a grey mesh upper with tonal jagged suede overlays and a reflective New Balance logo. From there, a cream Nrgy midsole and grey outsole complete the design. The New Balance 2002R Protection Pack Rain Cloud released in August of 2021.", "imageTag": "New Balance 2002R Protection Pack Rain Cloud.png" },
    { "name": "New Balance 9060 Crystal Pink", "price": "£160", "description": "The New Balance 9060 Crystal Pink takes the 9060's technical silhouette and applies a Pink Haze base with silver and off-white accents. The upper is made of breathable mesh with overlapping suede overlays that give the sneaker the illusion of layers. True to its technical roots, this running shoe features a chunky rubber sole with an ABZORB midsole and lightweight SBS cushioning. The oversized 'N' on the lateral side comes in silver leather and is outlined in white, while the 'N' on the medial side panel is made of suede with lines stitched across in silver thread. The lace cage houses tonal white laces that match the white outline surrounding the 'N.' Something our StockZ experts like is the incorporation of slightly off-white rubber on the outsole. It gives the sneaker a worn-in feel that contributes to its throwback aesthetic. The New Balance 9060 Crystal Pink was released on July 26th, 2023", "imageTag": "New Balance 9060 Crystal Pink.png" },
    { "name": "Adidas Samba OG Cloud White Core Black", "price": "£100", "description": "Originally designed to protect soccer players' feet during winter, the adidas Samba OG Cloud White Core Black has transcended its sports function but still maintains its aesthetic appeal. The adidas Samba OG Cloud White Core Black upper is built from full-grain leather with a light brown suede and dark brown heel tab providing contrast. Serrated 3-Stripes appear in deep brown on the lateral and medial sides, a Bluebird tongue label, and a foil logotype mark the shoe's DNA. Underfoot, a brown gum rubber outsole provides traction and durability. The adidas Samba OG Cloud White Core Black was released in January 2018", "imageTag": "Adidas Samba OG Cloud White Core Black.png" },
    { "name": "Adidas Yeezy Boost 350 V2 Bone", "price": "£230", "description": "The adidas Yeezy Boost 350 V2 Bone features a triple white Primeknit upper with mesh side stripes and canvas heel tabs. At the base, a semi-translucent sole with Boost technology completes the design. The adidas Yeezy Boost 350 V2 Bone released in March of 2022", "imageTag": "Adidas Yeezy Boost 350 V2 Bone.png" },
]

# sneaker_to_delete_name = "Jordan 1 Retro High OG Spider-Man Across the Spider-Verse"

with app.app_context():
    db.create_all()
    
    for sneaker in sneakers:
        existing_sneaker = Sneaker.query.filter_by(name=sneaker["name"]).first()
        if existing_sneaker is None:
            newSneaker = Sneaker(name=sneaker["name"], price=sneaker["price"], description=sneaker["description"], imageTag=sneaker["imageTag"])
            db.session.add(newSneaker)
            print(f"Added new sneaker: {sneaker['name']}")
        else:
            existing_sneaker.price = sneaker["price"]
            existing_sneaker.description = sneaker["description"]
            existing_sneaker.imageTag = sneaker["imageTag"]
            print(f"Updated existing sneaker: {sneaker['name']}")

    # Delete a sneaker (Use only when needed)
    # sneaker_to_delete = Sneaker.query.filter_by(name=sneaker_to_delete_name).first()
    # if sneaker_to_delete:
    #     db.session.delete(sneaker_to_delete)
    #     print(f"Deleted sneaker: {sneaker_to_delete.name}")

    db.session.commit()




