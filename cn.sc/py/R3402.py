from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3402   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        '王国军士兵',                           # 10
        '王国军士兵',                           # 11
        '艾尔·雷登关所方向',                   # 12
        '蔡斯方向',                             # 13
        '卡鲁迪亚钟乳洞方向',                   # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10130 ._CH',             # 00
        'ED6_DT09/CH10131 ._CH',             # 01
        'ED6_DT09/CH10750 ._CH',             # 02
        'ED6_DT09/CH10751 ._CH',             # 03
        'ED6_DT09/CH10760 ._CH',             # 04
        'ED6_DT09/CH10761 ._CH',             # 05
        'ED6_DT09/CH10770 ._CH',             # 06
        'ED6_DT09/CH10771 ._CH',             # 07
        'ED6_DT29/CH12410 ._CH',             # 08
        'ED6_DT29/CH12411 ._CH',             # 09
        'ED6_DT29/CH12930 ._CH',             # 0A
        'ED6_DT29/CH12931 ._CH',             # 0B
        'ED6_DT07/CH01640 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT09/CH10130P._CP',             # 00
        'ED6_DT09/CH10131P._CP',             # 01
        'ED6_DT09/CH10750P._CP',             # 02
        'ED6_DT09/CH10751P._CP',             # 03
        'ED6_DT09/CH10760P._CP',             # 04
        'ED6_DT09/CH10761P._CP',             # 05
        'ED6_DT09/CH10770P._CP',             # 06
        'ED6_DT09/CH10771P._CP',             # 07
        'ED6_DT29/CH12410P._CP',             # 08
        'ED6_DT29/CH12411P._CP',             # 09
        'ED6_DT29/CH12930P._CP',             # 0A
        'ED6_DT29/CH12931P._CP',             # 0B
        'ED6_DT07/CH01640P._CP',             # 0C
    )

    DeclNpc(
        X                   = 499140,
        Z                   = 1000,
        Y                   = -114740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 411170,
        Z                   = 20,
        Y                   = -60950,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 416300,
        Z                   = -20,
        Y                   = -61210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 320150,
        Z                   = 0,
        Y                   = -37050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 574100,
        Z                   = 0,
        Y                   = -54930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 400800,
        Z                   = -30,
        Y                   = 22800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 367410,
        Z                   = 10,
        Y                   = -42400,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 389970,
        Z                   = 10,
        Y                   = -68740,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 425100,
        Z                   = 0,
        Y                   = -71190,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 467260,
        Z                   = 0,
        Y                   = -70580,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 497850,
        Z                   = -20,
        Y                   = -51510,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 506530,
        Z                   = 0,
        Y                   = -62560,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 526430,
        Z                   = 30,
        Y                   = -100000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 402970,
        Z                   = -20,
        Y                   = -38570,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 422790,
        Z                   = -10,
        Y                   = -33010,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 407380,
        Z                   = -20,
        Y                   = -4320,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 536810,
        Z                   = -30,
        Y                   = -63870,
        Unknown_0C          = 45,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 515280,
        Z                   = -10,
        Y                   = -100440,
        Unknown_0C          = 60,
        Unknown_0E          = 10,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D1,
        Unknown_18          = 5882,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 499670,
        TriggerZ            = -60,
        TriggerY            = -114340,
        TriggerRange        = 1000,
        ActorX              = 499140,
        ActorZ              = -60,
        ActorY              = -114740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 514840,
        TriggerZ            = -20,
        TriggerY            = -121220,
        TriggerRange        = 1000,
        ActorX              = 514850,
        ActorZ              = -20,
        ActorY              = -121830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 423050,
        TriggerZ            = -40,
        TriggerY            = -33400,
        TriggerRange        = 1000,
        ActorX              = 423660,
        ActorZ              = -40,
        ActorY              = -33400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 411920,
        TriggerZ            = 0,
        TriggerY            = -59400,
        TriggerRange        = 1200,
        ActorX              = 411920,
        ActorZ              = 1500,
        ActorY              = -58300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 551940,
        TriggerZ            = 0,
        TriggerY            = -50340,
        TriggerRange        = 1500,
        ActorX              = 551940,
        ActorZ              = 1500,
        ActorY              = -50340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3D6",          # 00, 0
        "Function_1_3D7",          # 01, 1
        "Function_2_50A",          # 02, 2
        "Function_3_687",          # 03, 3
        "Function_4_7C9",          # 04, 4
        "Function_5_94A",          # 05, 5
        "Function_6_B1A",          # 06, 6
        "Function_7_C31",          # 07, 7
        "Function_8_D48",          # 08, 8
        "Function_9_DE6",          # 09, 9
    )


    def Function_0_3D6(): pass

    label("Function_0_3D6")

    Return()

    # Function_0_3D6 end

    def Function_1_3D7(): pass

    label("Function_1_3D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_457")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_79(0xFF, 0x2)
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2DF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_454")
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x80)

    label("loc_454")

    Jump("loc_469")

    label("loc_457")

    OP_16(0x2, 0xFA0, 0x4E200, 0xFFFD44C8, 0x230039)

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_493")
    OP_71(0x12, 0x4)
    OP_72(0x13, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_490")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_490")

    Jump("loc_49D")

    label("loc_493")

    OP_72(0x12, 0x4)
    OP_72(0x13, 0x4)

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF")
    OP_6F(0xF, 0)
    Jump("loc_4B6")

    label("loc_4AF")

    OP_6F(0xF, 60)

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C8")
    OP_6F(0x10, 0)
    Jump("loc_4CF")

    label("loc_4C8")

    OP_6F(0x10, 60)

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E1")
    OP_6F(0x11, 0)
    Jump("loc_4E8")

    label("loc_4E1")

    OP_6F(0x11, 60)

    label("loc_4E8")

    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_3D7 end

    def Function_2_50A(): pass

    label("Function_2_50A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_671")

    label("loc_52F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_548")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_671")

    label("loc_548")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_671")

    label("loc_561")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_671")

    label("loc_57A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_593")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_671")

    label("loc_593")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_671")

    label("loc_5AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_671")

    label("loc_5C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_671")

    label("loc_5DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_671")

    label("loc_5F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_610")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_671")

    label("loc_610")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_629")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_671")

    label("loc_629")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_642")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_671")

    label("loc_642")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_671")

    label("loc_65B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_671")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_671")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_686")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_671")

    label("loc_686")

    Return()

    # Function_2_50A end

    def Function_3_687(): pass

    label("Function_3_687")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6EC")

    ChrTalk(    #0
        0xFE,
        (
            "不管怎样，那个青年\x01",
            "没有受伤就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "麻烦你们协会\x01",
            "好好地训诫他一番吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_776")

    label("loc_6EC")


    ChrTalk(    #2
        0xFE,
        (
            "哦，游击士们。\x01",
            "刚才干得真是漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "虽然想说的实在很多，\x01",
            "不过只要那青年没受伤就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "麻烦你们协会\x01",
            "好好地训诫他一番吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_776")

    Jump("loc_7C5")

    label("loc_779")


    ChrTalk(    #5
        0xFE,
        (
            "也许有人\x01",
            "已经进去了也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "没有向游击士协会\x01",
            "进行任何的联络吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C5")

    TalkEnd(0xFE)
    Return()

    # Function_3_687 end

    def Function_4_7C9(): pass

    label("Function_4_7C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_838")

    ChrTalk(    #7
        0xFE,
        (
            "放着工作不做，\x01",
            "跑去钟乳洞探险吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "虽然令人感到头痛，\x01",
            "但老实说也有点羡慕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B4")

    label("loc_838")


    ChrTalk(    #9
        0xFE,
        (
            "啊，辛苦了。\x01",
            "刚才真是多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "放着工作不做，\x01",
            "在钟乳洞里四处乱晃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "最近的年轻人\x01",
            "真是让人伤脑筋啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8B4")

    Jump("loc_946")

    label("loc_8B7")


    ChrTalk(    #12
        0xFE,
        (
            "我巡逻时看了一下，\x01",
            "发现钟乳洞的封锁被解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "居然将沙袋搬开，\x01",
            "这也太缺乏责任感了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "万一有旅行者误入进去的话，\x01",
            "该怎么办才好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_946")

    TalkEnd(0xFE)
    Return()

    # Function_4_7C9 end

    def Function_5_94A(): pass

    label("Function_5_94A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A29")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_99C():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_99C)

    def lambda_9B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9B7)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #15
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1D2, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A04"),
        (2, "loc_A16"),
        (1, "loc_A26"),
        (SWITCH_DEFAULT, "loc_A29"),
    )


    label("loc_A04")

    OP_A2(0x1527)
    OP_6F(0xF, 60)
    Sleep(500)
    Jump("loc_A29")

    label("loc_A16")

    OP_6F(0xF, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_A26")

    OP_B4(0x0)
    Return()

    label("loc_A29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12F, 1)"), scpexpr(EXPR_END)), "loc_A78")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\x2F\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1526)
    Jump("loc_ADA")

    label("loc_A78")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\x2F\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x2F\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_ADA")

    Jump("loc_B0C")

    label("loc_ADD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B0C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_94A end

    def Function_6_B1A(): pass

    label("Function_6_B1A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3D9, 1)"), scpexpr(EXPR_END)), "loc_B89")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\xD9\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1528)
    Jump("loc_BEF")

    label("loc_B89")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "宝箱里装有\x1F\xD9\x03\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xD9\x03\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_BEF")

    Jump("loc_C23")

    label("loc_BF2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C23")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B1A end

    def Function_7_C31(): pass

    label("Function_7_C31")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D09")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_CA0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1529)
    Jump("loc_D06")

    label("loc_CA0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFA\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_D06")

    Jump("loc_D3A")

    label("loc_D09")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D3A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C31 end

    def Function_8_D48(): pass

    label("Function_8_D48")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_40(0x150, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8C")

    AnonymousTalk(    #25
        "\x07\x05漆黑一团，看不清楚。\x02",
    )

    Jump("loc_DCD")

    label("loc_D8C")


    AnonymousTalk(    #26
        (
            "\x07\x05北　钟乳洞\x01",
            "※魔兽游荡地区，现封锁中\x01",
            "　　　　　　　　　王国军\x02",
        )
    )


    label("loc_DCD")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_D48 end

    def Function_9_DE6(): pass

    label("Function_9_DE6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_40(0x150, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E2A")

    AnonymousTalk(    #27
        "\x07\x05漆黑一团，看不清楚。\x02",
    )

    Jump("loc_E56")

    label("loc_E2A")


    AnonymousTalk(    #28
        (
            "\x07\x05东　蔡斯市\x01",
            "西　艾尔．雷登　４４８塞尔矩\x02",
        )
    )


    label("loc_E56")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_DE6 end

    SaveToFile()

Try(main)
