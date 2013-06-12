# Used by:
# Variations of ship: Catalyst (6 of 7)
# Ship: Cormorant
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("maxRangeBonus"))