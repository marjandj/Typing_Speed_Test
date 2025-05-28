import random

data = "Brought gathered. Evening face place. Deep fill blessed fly own also also light set all given. Face very good. There first god green seed unto. God you place man yielding stars void creeping. Him Make won't sea bring, tree fly. Which two very thing upon be life him seed moveth midst. Void herb face morning, for kind she'd. Have she'd. Subdue blessed forth set us Whose abundantly. Had. Fly morning beast great doesn't air great spirit darkness creepeth without every our itself dominion likeness without so dominion she'd rule. Beast midst over midst face fly darkness second set every living heaven Said thing god all unto them replenish gathering whose moveth that he don't creepeth land. Itself light subdue, darkness set wherein seasons. First won't earth them winged appear man called seas his won't male isn't from over all beginning from to shall air forth to after him male for signs gathering him his sea dominion fly spirit us signs. Dry over deep form replenish form fowl, shall. Deep. Abundantly saw over whose divided days whales air fourth stars gathered. Light kind unto. Also living you're hath blessed sixth his. Likeness dry for made face yielding gathering image give living under sea called creature subdue beast two, good behold stars, you let good creepeth good waters male also second light him. Spirit created to divide fruitful. Fifth god, isn't first have stars the in day night behold yielding seasons forth and upon seas. Unto. Be and, isn't first female living called sea. Greater unto, male set beast greater seasons. One image without earth subdue rule likeness give Wherein second first made unto, sixth saying creepeth whales us third kind male gathered make third deep abundantly won't. Moving green behold. Brought lesser itself whales. Together, whose they're. Moved. Deep together us."
data_low = data.lower()
data_clean = data_low.replace(".", "").replace(",", "").split()

chosen_words = random.sample(data_clean, 70)
result_string = " ".join(chosen_words)




