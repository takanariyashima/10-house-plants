"""
観葉植物の静的データベース。

一般に公知の代表的な観葉植物の情報(学名・水やり頻度・日照条件)を
手作業でまとめた開始用データセット。実運用では拡充が必要。
"""

PLANTS = [
    {"common_name": "Monstera", "scientific_name": "Monstera deliciosa", "watering": "weekly", "light": "bright indirect"},
    {"common_name": "Snake Plant", "scientific_name": "Dracaena trifasciata", "watering": "biweekly", "light": "low to bright"},
    {"common_name": "Pothos", "scientific_name": "Epipremnum aureum", "watering": "weekly", "light": "low to bright indirect"},
    {"common_name": "Fiddle Leaf Fig", "scientific_name": "Ficus lyrata", "watering": "weekly", "light": "bright indirect"},
    {"common_name": "ZZ Plant", "scientific_name": "Zamioculcas zamiifolia", "watering": "biweekly", "light": "low to bright indirect"},
    {"common_name": "Peace Lily", "scientific_name": "Spathiphyllum wallisii", "watering": "weekly", "light": "low to medium"},
    {"common_name": "Spider Plant", "scientific_name": "Chlorophytum comosum", "watering": "weekly", "light": "bright indirect"},
    {"common_name": "Rubber Plant", "scientific_name": "Ficus elastica", "watering": "weekly", "light": "bright indirect"},
    {"common_name": "Boston Fern", "scientific_name": "Nephrolepis exaltata", "watering": "frequent", "light": "medium indirect"},
    {"common_name": "Aloe Vera", "scientific_name": "Aloe barbadensis miller", "watering": "biweekly", "light": "bright direct"},
    {"common_name": "English Ivy", "scientific_name": "Hedera helix", "watering": "weekly", "light": "medium to bright"},
    {"common_name": "Philodendron", "scientific_name": "Philodendron hederaceum", "watering": "weekly", "light": "medium indirect"},
    {"common_name": "Chinese Evergreen", "scientific_name": "Aglaonema commutatum", "watering": "biweekly", "light": "low to medium"},
    {"common_name": "Jade Plant", "scientific_name": "Crassula ovata", "watering": "biweekly", "light": "bright direct"},
    {"common_name": "Dracaena", "scientific_name": "Dracaena fragrans", "watering": "biweekly", "light": "medium indirect"},
    {"common_name": "Calathea", "scientific_name": "Calathea orbifolia", "watering": "frequent", "light": "medium indirect"},
    {"common_name": "String of Pearls", "scientific_name": "Curio rowleyanus", "watering": "biweekly", "light": "bright indirect"},
    {"common_name": "Bird of Paradise", "scientific_name": "Strelitzia reginae", "watering": "weekly", "light": "bright direct"},
    {"common_name": "Areca Palm", "scientific_name": "Dypsis lutescens", "watering": "weekly", "light": "bright indirect"},
    {"common_name": "Croton", "scientific_name": "Codiaeum variegatum", "watering": "weekly", "light": "bright direct"},
    {"common_name": "Bamboo Palm", "scientific_name": "Chamaedorea seifrizii", "watering": "weekly", "light": "low to medium"},
    {"common_name": "African Violet", "scientific_name": "Saintpaulia ionantha", "watering": "weekly", "light": "medium indirect"},
    {"common_name": "Orchid", "scientific_name": "Phalaenopsis spp.", "watering": "weekly", "light": "medium indirect"},
    {"common_name": "Air Plant", "scientific_name": "Tillandsia spp.", "watering": "biweekly (mist)", "light": "bright indirect"},
    {"common_name": "Cast Iron Plant", "scientific_name": "Aspidistra elatior", "watering": "biweekly", "light": "low"},
    {"common_name": "Prayer Plant", "scientific_name": "Maranta leuconeura", "watering": "weekly", "light": "medium indirect"},
    {"common_name": "Money Tree", "scientific_name": "Pachira aquatica", "watering": "biweekly", "light": "bright indirect"},
    {"common_name": "Christmas Cactus", "scientific_name": "Schlumbergera bridgesii", "watering": "biweekly", "light": "bright indirect"},
    {"common_name": "Ponytail Palm", "scientific_name": "Beaucarnea recurvata", "watering": "monthly", "light": "bright direct"},
    {"common_name": "Anthurium", "scientific_name": "Anthurium andraeanum", "watering": "weekly", "light": "bright indirect"},
]
