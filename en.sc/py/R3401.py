from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3401   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3401.x',
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
        'Measuring Device',                     # 9
        'Anelace',                              # 10
        'Agate',                                # 11
        'Scherazard',                           # 12
        'Air-Letten - Checkpoint',              # 13
        'Zeiss',                                # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT06/CH20020 ._CH',             # 0A
        'ED6_DT07/CH00065 ._CH',             # 0B
        'ED6_DT27/CH03090 ._CH',             # 0C
        'ED6_DT06/CH20053 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT27/CH03091 ._CH',             # 0F
        'ED6_DT26/CH20284 ._CH',             # 10
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
        'ED6_DT06/CH20020P._CP',             # 0A
        'ED6_DT07/CH00065P._CP',             # 0B
        'ED6_DT27/CH03090P._CP',             # 0C
        'ED6_DT06/CH20053P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT27/CH03091P._CP',             # 0F
        'ED6_DT26/CH20284P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 169300,
        Z                   = 0,
        Y                   = -27030,
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
        X                   = 330710,
        Z                   = 0,
        Y                   = -37560,
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
        X                   = 257600,
        Z                   = 70,
        Y                   = -24310,
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
        X                   = 286240,
        Z                   = 20,
        Y                   = -35830,
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
        X                   = 215540,
        Z                   = 0,
        Y                   = -31930,
        Unknown_0C          = 90,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 275760,
        Y                   = -2000,
        Z                   = -27140,
        Range               = 280150,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF7482,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = 257600,
        TriggerZ            = -70,
        TriggerY            = -24310,
        TriggerRange        = 3000,
        ActorX              = 257600,
        ActorZ              = -70,
        ActorY              = -24310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 284880,
        TriggerZ            = 50,
        TriggerY            = -26870,
        TriggerRange        = 1000,
        ActorX              = 284880,
        ActorZ              = 1050,
        ActorY              = -26870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 267860,
        TriggerZ            = 0,
        TriggerY            = -29500,
        TriggerRange        = 1000,
        ActorX              = 268340,
        ActorZ              = 0,
        ActorY              = -25650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D2",          # 00, 0
        "Function_1_2D3",          # 01, 1
        "Function_2_408",          # 02, 2
        "Function_3_A11",          # 03, 3
        "Function_4_BE0",          # 04, 4
        "Function_5_C19",          # 05, 5
        "Function_6_C52",          # 06, 6
        "Function_7_C8B",          # 07, 7
        "Function_8_4ED2",         # 08, 8
        "Function_9_4F6A",         # 09, 9
        "Function_10_4FD0",        # 0A, 10
        "Function_11_5221",        # 0B, 11
    )


    def Function_0_2D2(): pass

    label("Function_0_2D2")

    Return()

    # Function_0_2D2 end

    def Function_1_2D3(): pass

    label("Function_1_2D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34C")
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
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_79(0xFF, 0x2)
    OP_64(0x2, 0x1)
    OP_82(0x80, 0x0)
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    Jump("loc_34C")

    label("loc_34C")

    OP_16(0x2, 0xFA0, 0x1F018, 0xFFFD9AB8, 0x230038)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_371")
    OP_64(0x0, 0x1)
    Jump("loc_375")

    label("loc_371")

    OP_65(0x0, 0x1)

    label("loc_375")

    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7")
    OP_72(0x12, 0x4)
    OP_72(0x13, 0x4)
    OP_72(0x14, 0x4)
    OP_72(0x15, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x50)

    label("loc_3A7")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_407")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, 284880, 1050, -26870, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_407")

    Return()

    # Function_1_2D3 end

    def Function_2_408(): pass

    label("Function_2_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_415")
    Return()

    label("loc_415")

    EventBegin(0x0)
    OP_A2(0x141A)
    Fade(1000)
    OP_6D(279460, 150, -31510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x101, 279920, 150, -32780, 0)
    SetChrPos(0xF7, 278990, 150, -31880, 42)
    SetChrPos(0x107, 279800, 150, -30480, 188)
    SetChrPos(0xF9, 281010, 0, -31850, 321)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1011F#5PLet's see...\x02\x03",

            "This is the place we're after--the first\x01",
            "bridge in the Kaldia Tunnel, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x107,
        (
            "#061FUh-huh! We just need to set up on\x01",
            "either side of the bridge, I think.\x02\x03",

            "#064FUm...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(500)
    OP_8C(0x107, 90, 400)
    OP_8C(0x107, 45, 400)
    Sleep(500)
    OP_8C(0x101, 50, 400)
    OP_8C(0xF7, 50, 400)
    OP_8C(0xF9, 50, 400)

    ChrTalk(    #2
        0x107,
        (
            "#060FThere's an orbal charging device\x01",
            "over here, so this is a bad spot.\x02\x03",

            "Which means...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(500)

    def lambda_60E():

        label("loc_60E")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_60E")

    QueueWorkItem2(0x101, 1, lambda_60E)

    def lambda_61F():

        label("loc_61F")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_61F")

    QueueWorkItem2(0xF7, 1, lambda_61F)

    def lambda_630():

        label("loc_630")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_630")

    QueueWorkItem2(0xF9, 1, lambda_630)

    def lambda_641():
        OP_8E(0xFE, 0x3F854, 0x0, 0xFFFF88AA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_641)

    def lambda_65C():
        OP_6D(271840, 150, -30100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_65C)

    def lambda_674():
        OP_67(0, 8330, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_674)
    Sleep(3500)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)

    def lambda_699():
        OP_8E(0xFE, 0x3F98A, 0xFFFFFFF6, 0xFFFF89E0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_699)
    Fade(1000)
    OP_6D(259010, 20, -28410, 0)
    OP_67(0, 8330, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0x4)
    Sleep(200)
    OP_43(0xF7, 0x0, 0x0, 0x5)
    Sleep(200)
    OP_43(0xF9, 0x0, 0x0, 0x6)
    WaitChrThread(0x107, 0x1)

    def lambda_72B():
        OP_8E(0xFE, 0x3EF76, 0x32, 0xFFFF9AB6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_72B)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_8C(0x107, 297, 400)
    Sleep(500)

    ChrTalk(    #3
        0x107,
        (
            "#064F#6POkay, and point the antenna\x01",
            "down the tunnel juuuust so...\x02\x03",

            "#060FYeah... This should be okay!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)
    OP_8C(0x107, 140, 400)

    ChrTalk(    #4
        0x107,
        (
            "#061F#6PEstelle, putting the device here\x01",
            "should work!\x02\x03",

            "Should I set it up?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Up Instrument\x01",      # 0
            "Not Yet\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D5")

    ChrTalk(    #5
        0x107,
        (
            "#061F#6POkay, I'll start setting it up.\x02\x03",

            "Gimme juuuust a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A01")

    label("loc_8D5")


    ChrTalk(    #6
        0x107,
        (
            "#064F#6PUm, we're not gonna set it up yet?\x02\x03",

            "#060FWell, once you're ready,\x01",
            "just examine this area again.\x02\x03",

            "I'll set it up, then!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(261190, -20, -31590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 259760, 0, -30960, 270)
    SetChrPos(0x1, 259760, 0, -30960, 270)
    SetChrPos(0x2, 259760, 0, -30960, 270)
    SetChrPos(0x3, 259760, 0, -30960, 270)
    OP_69(0x0, 0x0)
    OP_65(0x0, 0x1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_A01")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 7)
    Return()

    # Function_2_408 end

    def Function_3_A11(): pass

    label("Function_3_A11")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(257060, 50, -25420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 256130, 30, -26520, 45)
    SetChrPos(0xF7, 257709, 50, -25940, 315)
    SetChrPos(0x107, 256660, 40, -25120, 45)
    SetChrPos(0xF9, 255050, 0, -25780, 47)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Up Instrument\x01",      # 0
            "Not Yet\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B42")

    ChrTalk(    #7
        0x107,
        (
            "#061F#6POkay, I'll start setting it up.\x02\x03",

            "Gimme juuuust a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD0")

    label("loc_B42")

    OP_8C(0x107, 225, 400)

    ChrTalk(    #8
        0x107,
        (
            "#064F#6PUm, we're not gonna set it up yet?\x02\x03",

            "#060FWell, once you're ready,\x01",
            "just examine this area again.\x02\x03",

            "I'll set it up, then!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_BD0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 7)
    Return()

    # Function_3_A11 end

    def Function_4_BE0(): pass

    label("Function_4_BE0")

    SetChrPos(0x101, 270570, 0, -31410, 265)

    def lambda_BF7():
        OP_8E(0xFE, 0x3F6B0, 0x0, 0xFFFF8710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF7)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 323, 400)
    Return()

    # Function_4_BE0 end

    def Function_5_C19(): pass

    label("Function_5_C19")

    SetChrPos(0xF7, 271930, 0, -30560, 268)

    def lambda_C30():
        OP_8E(0xFE, 0x3FBA5, 0xFFFFFFE2, 0xFFFF8A4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C30)
    WaitChrThread(0xF7, 0x1)
    OP_8C(0xF7, 323, 400)
    Return()

    # Function_5_C19 end

    def Function_6_C52(): pass

    label("Function_6_C52")

    SetChrPos(0xF9, 272280, 0, -32150, 272)

    def lambda_C69():
        OP_8E(0xFE, 0x3FC50, 0xFFFFFFEC, 0xFFFF83D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_C69)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0xF9, 323, 400)
    Return()

    # Function_6_C52 end

    def Function_7_C8B(): pass

    label("Function_7_C8B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(257060, 50, -25420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(80000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 256130, 30, -26520, 45)
    SetChrPos(0xF7, 257709, 50, -25940, 315)
    SetChrPos(0x107, 256660, 40, -25120, 45)
    SetChrPos(0xF9, 255050, 0, -25780, 47)
    OP_72(0x12, 0x4)
    OP_72(0x13, 0x4)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #9
        0x107,
        "#061F#6PAll done!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E91")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Make this the first instrument set\x01",                                  # 0
            "Make Tratt Plains instrument already set\x01",                            # 1
            "Make Leiston Fortress instrument already set\x01",                        # 2
            "Make Tratt Plains and Leiston Fortress instruments already set\x01",      # 3
            "No change\x01",                                                           # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E61"),
        (1, "loc_E6D"),
        (2, "loc_E79"),
        (3, "loc_E85"),
        (SWITCH_DEFAULT, "loc_E91"),
    )


    label("loc_E61")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_E91")

    label("loc_E6D")

    OP_A2(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_E91")

    label("loc_E79")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A2(0x141F)
    Jump("loc_E91")

    label("loc_E85")

    OP_A2(0x1419)
    OP_A3(0x141B)
    OP_A2(0x141F)
    Jump("loc_E91")

    label("loc_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14FC")

    ChrTalk(    #10
        0x101,
        (
            "#1004F#2PWhoa, so this is what it looks like\x01",
            "when it's all together? Wow!\x02\x03",

            "#1015FWhat's, um...this dish-like thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 225, 400)

    ChrTalk(    #11
        0x107,
        (
            "#060F#6POh, that's a kind of antenna for\x01",
            "broadcasting orbal-waves called\x01",
            "a parabolic antenna!\x02\x03",

            "It puts out really powerful orbal waves\x01",
            "that can cover really long distances...\x02\x03",

            "It can even broadcast from inside\x01",
            "a place like the Kaldia Tunnel!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1211")
    OP_8C(0x104, 90, 400)

    ChrTalk(    #12
        0x104,
        (
            "#033F#5PHmmmm... A most impressive tool.\x02\x03",

            "#030FI don't recall seeing anything like\x01",
            "this at the corner tool shop...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #13
        0x107,
        (
            "#560F#6PWell, I don't think it's\x01",
            "for sale anywhere yet...\x02\x03",

            "It's one of Grandpa's inventions, though,\x01",
            "so I bet the central factory will start\x01",
            "selling them pretty soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x104,
        "#031F#5PMmm. Lovely.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_120E")
    OP_8C(0x103, 270, 400)

    ChrTalk(    #15
        0x103,
        (
            "#027F#4POlivier, is that your...interest in\x01",
            "technology showing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x104,
        (
            "#035F#5PWhy, whatever do you mean, dear\x01",
            "Schera? I certainly don't know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120E")

    Jump("loc_13EF")

    label("loc_1211")

    OP_8C(0x105, 90, 400)

    ChrTalk(    #17
        0x105,
        (
            "#044F#5PUm, Tita?\x02\x03",

            "I'd heard that orbal waves weaken\x01",
            "as they pass through obstacles.\x02\x03",

            "Are we really going to be able to get\x01",
            "a signal out of the tunnel?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #18
        0x107,
        (
            "#560F#6POh, um, according to Grandpa,\x01",
            "the antenna can direct orbal waves.\x02\x03",

            "So even if you're in a cave, you can\x01",
            "reflect it down the tunnel and bounce\x01",
            "it off the walls until it reaches the exit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        (
            "#040F#5PI see! My goodness...\x02\x03",

            "#041FProfessor Russell really is as much\x01",
            "of a genius as he's ever been.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EF")


    ChrTalk(    #20
        0x101,
        (
            "#1007F#2PI guess I'm too much of a country girl\x01",
            "to appreciate how incredible it is...\x02\x03",

            "#1006FThis thing'll transmit earthquake\x01",
            "info back to us, though, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 225, 400)

    ChrTalk(    #21
        0x107,
        (
            "#560F#6PUm, not yet.\x01",
            "I haven't started it up yet.\x02\x03",

            "Just need to flip the switch...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)
    Jump("loc_1552")

    label("loc_14FC")


    ChrTalk(    #22
        0x101,
        (
            "#1006F#2PWell, flip that switch\x01",
            "as hard as you can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        "#560F#6PFlipping...NOW!\x02",
    )

    CloseMessageWindow()

    label("loc_1552")

    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 11)
    OP_0D()
    OP_8C(0xF7, 315, 400)
    OP_8C(0xF9, 45, 400)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x14, 0x4)
    OP_72(0x15, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x50)
    Sleep(2000)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1719")
    OP_8C(0x107, 225, 400)

    ChrTalk(    #24
        0x107,
        "#061F#6PYay! ♪ Now it works!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1006F#2PGreat work, Tita!\x02\x03",

            "#1015FAlthough...is it really okay to just leave\x01",
            "it here? Won't it get attacked by monsters?\x02\x03",

            "The antenna looks easy to break, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x107,
        (
            "#560F#6POh, it'll be okay.\x02\x03",

            "When it's powered on, it repels monsters\x01",
            "like the street lamps do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1011F#2POh, okay. That works, then!\x02",
    )

    CloseMessageWindow()
    Jump("loc_177F")

    label("loc_1719")

    OP_8C(0x107, 225, 400)

    ChrTalk(    #28
        0x107,
        "#061F#6PYay! ♪ Now it works!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_176A")

    ChrTalk(    #29
        0x106,
        "#051FGood work, squirt.\x02",
    )

    CloseMessageWindow()
    Jump("loc_177F")

    label("loc_176A")


    ChrTalk(    #30
        0x103,
        "#021FWell done.\x02",
    )

    CloseMessageWindow()

    label("loc_177F")

    SetChrPos(0x9, 269420, 0, -30490, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17B5")
    SetChrPos(0xB, 269390, 0, -31690, 0)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_17CB")

    label("loc_17B5")

    SetChrPos(0xA, 269390, 0, -31690, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_17CB")


    NpcTalk(    #31
        0x9,
        "Girl's Voice",
        (
            "#3PHeeeeeeey!\x01",
            "Esteeeeeelle!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 135, 400)

    ChrTalk(    #32
        0x101,
        "#1004F#5PHuh?!\x02",
    )

    CloseMessageWindow()

    def lambda_1836():

        label("loc_1836")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1836")

    QueueWorkItem2(0xF7, 1, lambda_1836)

    def lambda_1847():

        label("loc_1847")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1847")

    QueueWorkItem2(0x107, 1, lambda_1847)

    def lambda_1858():

        label("loc_1858")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1858")

    QueueWorkItem2(0xF9, 1, lambda_1858)

    def lambda_1869():
        OP_6D(258339, 30, -28020, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1869)

    def lambda_1881():
        OP_67(0, 8300, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1881)

    def lambda_1899():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_1899)

    def lambda_18A9():
        OP_8E(0x9, 0x3FA29, 0xFFFFFFF6, 0xFFFF88E6, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18A9)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_18E8")

    def lambda_18D0():
        OP_8E(0xB, 0x3FA3E, 0x1E, 0xFFFF8436, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18D0)
    Jump("loc_1903")

    label("loc_18E8")


    def lambda_18EE():
        OP_8E(0xA, 0x3FA3E, 0x1E, 0xFFFF8436, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_18EE)

    label("loc_1903")

    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x9, 0x1)

    def lambda_1913():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1913)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1960")

    ChrTalk(    #33
        0x101,
        "#1004F#5PAnelace! And Schera, too!\x02",
    )

    WaitChrThread(0xB, 0x2)

    def lambda_1954():
        TurnDirection(0xB, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1954)
    CloseMessageWindow()
    Jump("loc_19AC")

    label("loc_1960")


    ChrTalk(    #34
        0x101,
        "#1004F#5PAnelace! And Agate, too!\x02",
    )

    WaitChrThread(0xA, 0x2)

    def lambda_1991():
        TurnDirection(0xA, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1991)
    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        "#064F#5PHuh?\x02",
    )

    CloseMessageWindow()

    label("loc_19AC")

    OP_44(0x107, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_19BE():
        OP_8E(0xFE, 0x3F534, 0x14, 0xFFFF8FC6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_19BE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1AC0")
    Sleep(50)

    def lambda_19E5():
        OP_8E(0xFE, 0x3EBBF, 0x14, 0xFFFF91F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19E5)
    Sleep(50)

    def lambda_1A05():
        OP_8E(0xFE, 0x3F0A1, 0x0, 0xFFFF8CBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1A05)
    Sleep(200)

    def lambda_1A25():
        OP_8E(0xFE, 0x3F2D1, 0x0, 0xFFFF95E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1A25)
    Sleep(100)

    def lambda_1A45():
        OP_8E(0xFE, 0x3EBE8, 0x14, 0xFFFF96BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1A45)
    Sleep(100)

    def lambda_1A65():
        OP_8E(0xFE, 0x3E60C, 0x14, 0xFFFF9444, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1A65)
    WaitChrThread(0x9, 0x0)

    def lambda_1A85():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1A85)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 135, 400)
    WaitChrThread(0xF7, 0x0)
    OP_8C(0xF7, 225, 400)
    WaitChrThread(0x107, 0x0)
    OP_8C(0x107, 135, 400)
    WaitChrThread(0xF9, 0x0)
    OP_8C(0xF9, 135, 400)
    Jump("loc_1BC7")

    label("loc_1AC0")

    Sleep(50)

    def lambda_1ACB():
        OP_8E(0xFE, 0x3EBBF, 0x14, 0xFFFF91F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1ACB)
    Sleep(50)

    def lambda_1AEB():
        OP_8E(0xFE, 0x3F0A1, 0x0, 0xFFFF8CBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1AEB)
    Sleep(200)

    def lambda_1B0B():
        OP_8E(0xFE, 0x3F2D1, 0x0, 0xFFFF95E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1B0B)
    Sleep(100)

    def lambda_1B2B():
        OP_8E(0xFE, 0x3EBE8, 0x14, 0xFFFF96BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1B2B)
    Sleep(100)

    def lambda_1B4B():
        OP_8E(0xFE, 0x3E60C, 0x14, 0xFFFF9444, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1B4B)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 135, 400)
    WaitChrThread(0x9, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B89")

    def lambda_1B7E():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B7E)
    Jump("loc_1B97")

    label("loc_1B89")


    def lambda_1B8F():
        TurnDirection(0x9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B8F)

    label("loc_1B97")

    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 135, 400)
    WaitChrThread(0xF7, 0x0)
    OP_8C(0xF7, 225, 400)
    WaitChrThread(0x107, 0x0)
    OP_8C(0x107, 135, 400)
    WaitChrThread(0xF9, 0x0)
    OP_8C(0xF9, 135, 400)

    label("loc_1BC7")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_35BC")

    ChrTalk(    #36
        0x9,
        (
            "#811F#4PHeheh! It's been a while!\x02\x03",

            "I didn't think we'd meet up\x01",
            "here of all places.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB0")

    ChrTalk(    #37
        0xB,
        (
            "#021FAnd I see a familiar face caught\x01",
            "up with you as well!\x02\x03",

            "#020FWeren't you staying at the hot springs\x01",
            "in Elmo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x104,
        (
            "#035F#5PAh, but Schera, there are currents\x01",
            "deeper than the sea at play here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "#027FMeaning you're tagging along\x01",
            "out of curiosity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1016F#5PPretty much, yeah.\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #41
        0x104,
        (
            "#036F#5PAh, the barbs and slings\x01",
            "I endure from you two...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1DB0")


    ChrTalk(    #42
        0xB,
        (
            "#021FThis is certainly a coincidence.\x02\x03",

            "#023FWait... Oh, my. Is that Princess\x01",
            "Klaudia with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x105,
        (
            "#041F#5PPlease, Scherazard, it's Kloe. And hello!\x02\x03",

            "#542FEstelle and I met again in Ruan,\x01",
            "and I've been trying to lend a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xB,
        (
            "#027FI see. Well, thank you for helping\x01",
            "Estelle, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        (
            "#048F#5PHaha, no, no, I really\x01",
            "don't need thanks...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0C")


    ChrTalk(    #46
        0x107,
        (
            "#560F#5PUmmmmm...\x01",
            "Hi, Schera, it's been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        "#814F#4POh...my...\x02",
    )

    OP_9E(0x9, 0x14, 0x0, 0x1F4, 0xFA0)
    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 600)

    ChrTalk(    #48
        0xB,
        (
            "#023FAnd Tita's here, too?\x02\x03",

            "#021FAh, right! Kilika mentioned getting Professor\x01",
            "Russell's help in investigating the earthquakes.\x02\x03",

            "You must be helping with that, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#067F#5PHeehee! Yep!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        "#1317F#4P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        (
            "#1015F#5PUh, Anelace?\x02\x03",

            "What's up? You're spacing out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "#1316F#4PI...c-c...can't...\x02\x03",

            "#812FI CAN'T STOP MYSELF ANYMORE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1004F#5PBuh?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_2104():
        OP_6D(257339, 30, -27020, 1000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2104)

    def lambda_211C():

        label("loc_211C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_211C")

    QueueWorkItem2(0x101, 1, lambda_211C)

    def lambda_212D():

        label("loc_212D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_212D")

    QueueWorkItem2(0xF7, 1, lambda_212D)

    def lambda_213E():

        label("loc_213E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_213E")

    QueueWorkItem2(0xF9, 1, lambda_213E)
    SetChrChipByIndex(0x9, 15)
    OP_92(0x9, 0x107, 0x190, 0x1388, 0x0)

    def lambda_2162():
        OP_94(0x1, 0x9, 0x0, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2162)
    OP_48()
    OP_8C(0x9, 315, 0)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 16)
    SetChrSubChip(0x9, 0)
    TurnDirection(0x107, 0x9, 0)
    OP_94(0x1, 0x107, 0xB4, 0xC8, 0x7D0, 0x0)
    WaitChrThread(0x9, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(200)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x9, 1)
    OP_0D()

    ChrTalk(    #54
        0x9,
        (
            "#1311F#4PYou...are...the...\x01",
            "CUTE-EST THIIIIIIIIIIIING!\x02\x03",

            "I can't NOT hug you!\x01",
            "So cute so cute so cuuuuuute!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #55
        0x107,
        "#064F#6PWawawawawawawawaaa?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1016F(Oh...uh...right...)\x02\x03",

            "(Anelace's love of cute things...\x01",
            "Didn't I, uh, call this at one point?\x01",
            "Gotta make sure she doesn't smother Tita...)\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #57
        0x9,
        (
            "#811F#4PYou said your name is Tita, right?\x01",
            "I'm Anelace Elfead!\x02\x03",

            "You just call me Anelace, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x107,
        "#065F#6PWh-Whaaaaa...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x9, 1)
    OP_0D()

    ChrTalk(    #59
        0x9,
        (
            "#819F#4PAaaaaaaaaah you're even CUTER when\x01",
            "you get all confused!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 12)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 257260, 20, -27260, 315)
    OP_0D()
    OP_8C(0x9, 135, 400)
    OP_8C(0x101, 45, 400)

    ChrTalk(    #60
        0x9,
        (
            "#812F#6PSchera!\x01",
            "I claim this cutie for the Bracer Guild!\x01",
            "We're taking her with us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "#027FI know how you feel, but I, ah,\x01",
            "don't think it's a good idea.\x02\x03",

            "If I were you, I'd be worried about\x01",
            "her big brother over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 225, 400)

    ChrTalk(    #62
        0x106,
        "#552F#6P...What are you starin' at me for?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    OP_8C(0xF9, 135, 400)

    ChrTalk(    #63
        0x101,
        (
            "#1011F#6PSo, uh, Schera.\x01",
            "Why are you guys out here?\x02\x03",

            "Did you come looking for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "#020FNo, this is just a happy coincidence.\x02\x03",

            "We're on the trail of some clues concerning\x01",
            "the sky bandits and the old Intelligence\x01",
            "Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x101,
        (
            "#1020F#6PHuh?\x02\x03",

            "The sky bandits and the Intelli...\x01",
            "You mean there are guys from\x01",
            "those still on the loose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x106,
        (
            "#052F#6PThat's right, there's still men from\x01",
            "both that the army hasn't caught.\x02\x03",

            "You guys found some kind of clue?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2773():
        OP_6D(258339, 30, -28020, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2773)
    OP_8E(0x9, 0x3F534, 0x14, 0xFFFF8FC6, 0x9C4, 0x0)
    TurnDirection(0x9, 0x107, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #67
        0x9,
        (
            "#810FWell, the guild's had witness calls pouring in.\x02\x03",

            "Most of them aren't all that reliable, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "#020FWe've been investigating throughout\x01",
            "the country, following up on some of\x01",
            "the more reliable leads.\x02\x03",

            "#022FThough...I was curious.\x02\x03",

            "I heard one of the Ouroboros showed\x01",
            "up in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1007F#5PYeah...\x02\x03",

            "#1019FA weirdo in an opera suit calling\x01",
            "himself the 'Phantom Thief.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x106,
        (
            "#555F#6PEven with that stupid costume...\x01",
            "guy was a powerhouse.\x02\x03",

            "If he'd really tried to fight us,\x01",
            "it could've been bad for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#812FWhoa... Agate's saying someone\x01",
            "was tough?\x02\x03",

            "Ouroboros really is dangerous,\x01",
            "in that case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "#026FMore 'mysterious' than 'dangerous,' I'd say...\x02\x03",

            "#020FWell, remember, if you need\x01",
            "our help, call us any time.\x02\x03",

            "If you use the guild's orbal phones,\x01",
            "you should be able to contact us\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1006F#5PYeah, we'll do that.\x02\x03",

            "Ditto for you, Schera--if anything happens,\x01",
            "get in touch with us.\x02\x03",

            "We'll be there in an instant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        (
            "#021FGood! I'll be counting on it.\x02\x03",

            "#027FIt is nice to see you again, but this\x01",
            "is hardly the place for a long talk...\x02\x03",

            "It's about time we moved on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1017F#5POh, yeah... It's too bad, but\x01",
            "I guess you're right.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF8")

    ChrTalk(    #76
        0x104,
        (
            "#036F#5POh, how cruel you are, Schera!\x02\x03",

            "How can you be so cold after finally\x01",
            "reuniting with your beloved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xB,
        (
            "#021FOhhh? Well, then.\x01",
            "Why don't you come with us?\x02\x03",

            "We can have a drink tonight\x01",
            "to celebrate our reunion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#811FOh, heeeeeey! ♪ Schera can drink a\x01",
            "dinedile under the table, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x104,
        "#034F#5P...Be cautious in your travels.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1019F#5POh, for... Why do you always try to do\x01",
            "things that blow up in your face?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF8")


    ChrTalk(    #81
        0x106,
        (
            "#050F#6PHey, don't take this the wrong way,\x01",
            "but you're two women traveling alone.\x02\x03",

            "Make sure you don't bite off\x01",
            "more than you can chew, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "#814FWhoa, whoa, Agate?\x01",
            "Being thoughtful?\x02\x03",

            "Hold the presses, I think the\x01",
            "earth just shook again!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #83
        0x106,
        (
            "#552F#6P...What DID I just say about\x01",
            "biting off and chewin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        "#1315FHeeheehee... Juuust kidding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xB,
        (
            "#027FHe does have a point, though.\x01",
            "Thank you, Agate. We'll be careful,\x01",
            "as should you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "#1310FStay well, everyone!\x02\x03",

            "#811FEstelle, Tita! Next time we meet,\x01",
            "let's hang out together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1006F#5PYou bet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x107,
        "#560F#5PUmmmm... Goodbye!\x02",
    )

    CloseMessageWindow()

    def lambda_306F():

        label("loc_306F")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_306F")

    QueueWorkItem2(0x101, 1, lambda_306F)

    def lambda_3080():

        label("loc_3080")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3080")

    QueueWorkItem2(0xF7, 1, lambda_3080)

    def lambda_3091():

        label("loc_3091")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3091")

    QueueWorkItem2(0x107, 1, lambda_3091)

    def lambda_30A2():

        label("loc_30A2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_30A2")

    QueueWorkItem2(0xF9, 1, lambda_30A2)

    def lambda_30B3():
        OP_8E(0xFE, 0x3B6D2, 0x0, 0xFFFF9C3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_30B3)
    Sleep(200)

    def lambda_30D3():
        OP_8E(0xFE, 0x3E8AA, 0xA, 0xFFFF8DFA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_30D3)
    WaitChrThread(0x9, 0x1)

    def lambda_30F3():
        OP_6D(255210, 20, -27320, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_30F3)

    def lambda_310B():
        OP_8E(0xFE, 0x3B6D2, 0x0, 0xFFFF9C3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_310B)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    Fade(500)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(257070, 20, -26960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF7, 257800, 30, -27320, 270)
    OP_0D()
    OP_8C(0x101, 0, 400)
    OP_8C(0x107, 180, 400)
    OP_8C(0xF9, 90, 400)

    ChrTalk(    #89
        0x101,
        (
            "#1017F#4PMmmmm... I didn't think we'd meet up\x01",
            "with Schera and Anelace out here.\x02\x03",

            "#1004FOh, Tita...are you okay?\x02\x03",

            "I was kind of afraid Anelace would\x01",
            "squeeze you like a grape...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x107,
        (
            "#067FHeehee! Yeah, I'm okay!\x02\x03",

            "That was...kind of surprising,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1016F#4PAh, well, um, she's not a BAD person,\x01",
            "so forgive her, okay?\x02\x03",

            "#1015FStill, though...remnants of the bandits\x01",
            "AND the Intelligence goons...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x106,
        (
            "#051FBoth groups seem to have\x01",
            "secret society backing.\x02\x03",

            "If those two do a good job,\x01",
            "we might get some valuable clues.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)
    OP_8C(0x107, 90, 400)

    ChrTalk(    #93
        0x101,
        (
            "#1006F#6PWe'd better do our best, too.\x02\x03",

            "#1011FAnyway...so right here is fine, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3484")

    ChrTalk(    #94
        0x106,
        (
            "#051FShould be. Let's get the\x01",
            "rest of the stuff set up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1006F#6PRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_35B9")

    label("loc_3484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34F0")

    ChrTalk(    #96
        0x106,
        (
            "#051FYeah. That's two devices down.\x02\x03",

            "Let's go set up the last one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1006F#6POkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_35B9")

    label("loc_34F0")


    ChrTalk(    #98
        0x106,
        (
            "#051FYeah. We've got all the devices\x01",
            "in place now, too.\x02\x03",

            "Let's get back to Gramps in the\x01",
            "Operations room at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1006F#6PRoger that. Fifth floor of the factory, right?\x02",
    )

    OP_28(0x87, 0x1, 0x200)
    CloseMessageWindow()

    label("loc_35B9")

    Jump("loc_4EC2")

    label("loc_35BC")


    ChrTalk(    #100
        0x9,
        "#811F#4PEstelle! Schera! It's been a while!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x103,
        "#021F#6PYeah! It certainly has. You look well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "#051FWhat the heck, you guys got a friggin'\x01",
            "family goin' here at this point.\x02\x03",

            "#052FEven Tita's here.\x02\x03",

            "#051FBeen a while, shortstuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #103
        0x107,
        (
            "#062F#5PAww, 'shortstuff'? That's mean!\x02\x03",

            "#560FBut...it has been a while, yeah...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #104
        0x9,
        (
            "#814FWh... What the?! She's so cute!\x02\x03",

            "#1310FWho is this cutie-pie?!\x01",
            "Estelle, have you been holding out on me in\x01",
            "the cute sister department or something?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1016F#5PAhaha... You could kinda say that,\x01",
            "I guess, yeah.\x02\x03",

            "#1006FThis is Tita, the granddaughter\x01",
            "of Professor Russell of Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "#810FThat right? Cool!\x02\x03",

            "#811FI'm Anelace, Anelace Elfead!\x02\x03",

            "Nice to meet you, Tita!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x107,
        "#560F#5PUm, yeah! Nice to meet you too!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9E")

    ChrTalk(    #108
        0xA,
        (
            "#555FOh, and...the Erebonian's with you.\x01",
            "Great.\x02\x03",

            "What are you doing here, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x104,
        (
            "#035F#5PWhat a silly question, my good Raven.\x02\x03",

            "#037FDo I need a reason to help\x01",
            "lovely damsels in their trials?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "#552FMan. You guys, uh...\x01",
            "kinda got it hard, it looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x103,
        "#027F#6POh, it's manageable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1007F#5PNot quite sure I'd say that...\x02\x03",

            "#1011FAnyway, what are you two\x01",
            "doing out here, Agate?\x02\x03",

            "Did you come looking for us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C12")

    label("loc_3A9E")


    ChrTalk(    #113
        0xA,
        (
            "#052FOh, and...the princess is with you.\x02\x03",

            "What're you doing with these guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x105,
        (
            "#041F#5PHaha. Please, Agate, call me Kloe.\x02\x03",

            "#542FActually, I've been assisting Estelle\x01",
            "ever since we met again in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "#051FHah, cool. You did seem like the\x01",
            "decisive type, back in the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1011F#5PSo what are you two doing out here, Agate?\x02\x03",

            "Did you come looking for us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C12")


    ChrTalk(    #117
        0xA,
        (
            "#051FNah, just a coincidence.\x02\x03",

            "We're in the middle of chasing down some\x01",
            "clues about the sky bandits and the\x01",
            "Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x101,
        (
            "#1020F#5PHuh?\x02\x03",

            "The sky bandits and the Intelli...\x01",
            "You mean there are guys from\x01",
            "those still on the loose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#023F#6PThat's right, there are men from both\x01",
            "still on the run from the army.\x02\x03",

            "Do you have a lead on their\x01",
            "whereabouts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "#810FWell, the guild's had witness calls pouring in.\x02\x03",

            "Most of them aren't all that reliable, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "#551FWe've been running around trying to\x01",
            "find the needles in the haystack.\x02\x03",

            "#050FMore importantly... I heard.\x02\x03",

            "You guys encountered one of Ouroboros'\x01",
            "henchmen in Ruan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1007F#5PYeah...\x02\x03",

            "#1019FA weirdo in an opera suit calling\x01",
            "himself the 'Phantom Thief.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x103,
        (
            "#022F#6PHis questionable fashion sense aside,\x01",
            "his power was...frankly, terrifying.\x02\x03",

            "If we'd tried to engage him directly,\x01",
            "I'm not sure it would've gone well for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "#812FWh-Whoa... That's the first time I've ever\x01",
            "heard Schera talk about someone like\x01",
            "that...\x02\x03",

            "Ouroboros really is dangerous,\x01",
            "in that case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        (
            "#552FMore like a total friggin' question\x01",
            "mark at this point...\x02\x03",

            "#050FAnyway, remember, you need our help,\x01",
            "just say the word.\x02\x03",

            "The guild'll be able to reach us easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1006F#5PYeah, we'll do that.\x02\x03",

            "Ditto for you, Agate--if anything happens,\x01",
            "get in touch with us.\x02\x03",

            "We'll be there in an instant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "#053FHeh, I think we'll be okay.\x01",
            "But I'll hold you to that if\x01",
            "it comes down to it.\x02\x03",

            "#051FAnyway, this ain't the best spot\x01",
            "for a leisurely chat, y'know?\x02\x03",

            "We oughtta get movin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1017F#5POh, yeah... I guess you're right.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x107)

    ChrTalk(    #129
        0x107,
        "#063F#5PU-Umm, Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        "#052FHm? Shortstuff?\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #131
        0x107,
        (
            "#560F#5PUm, well...\x02\x03",

            "...\x02\x03",

            "#562FNo, sorry... It's nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xA,
        (
            "#555FUh... Yeah, whatever.\x02\x03",

            "#051FAnyhow, give my best to Russell, will ya?\x02\x03",

            "And don't spend too much time\x01",
            "messin' with machines, okay?\x02\x03",

            "Make sure to find some time to be a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        (
            "#067F#5PHeehee! Okay!\x02\x03",

            "#560FBut, Agate, be careful, okay?\x02\x03",

            "You always do really dangerous things\x01",
            "because you're so stubborn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "#055FGkh...!\x01",
            "...Well, you've gotten good\x01",
            "at givin' it back, shortstuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x107,
        (
            "#067F#5PHeehee! Well, yeah!\x02\x03",

            "#066FI gotta...start growing up sometime,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x9,
        (
            "#811FHeehee! Agate can't lift a\x01",
            "finger against Tita, huh?\x02\x03",

            "#1310FWell, see you, guys!\x02\x03",

            "Estelle, Tita, let's hang out\x01",
            "when we get together next!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#1006F#5PYou bet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x107,
        "#560F#5PO-Okay!\x02",
    )

    CloseMessageWindow()

    def lambda_45B0():

        label("loc_45B0")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_45B0")

    QueueWorkItem2(0x107, 1, lambda_45B0)

    def lambda_45C1():

        label("loc_45C1")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_45C1")

    QueueWorkItem2(0xF7, 1, lambda_45C1)

    def lambda_45D2():

        label("loc_45D2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_45D2")

    QueueWorkItem2(0x101, 1, lambda_45D2)

    def lambda_45E3():

        label("loc_45E3")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_45E3")

    QueueWorkItem2(0xF9, 1, lambda_45E3)

    def lambda_45F4():
        OP_8E(0xFE, 0x3B6D2, 0x0, 0xFFFF9C3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_45F4)
    Sleep(200)

    def lambda_4614():
        OP_8E(0xFE, 0x3E8AA, 0xA, 0xFFFF8DFA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4614)
    WaitChrThread(0x9, 0x1)

    def lambda_4634():
        OP_6D(255210, 20, -27320, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4634)

    def lambda_464C():
        OP_8E(0xFE, 0x3B6D2, 0x0, 0xFFFF9C3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_464C)
    WaitChrThread(0xA, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    Fade(1000)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(257070, 20, -26960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF7, 257800, 30, -27320, 270)
    OP_0D()
    OP_8C(0x101, 45, 400)
    OP_8C(0xF9, 90, 400)

    ChrTalk(    #139
        0x101,
        (
            "#1017F#6P*sigh* Man, I didn't expect to\x01",
            "meet those two.\x02\x03",

            "#1016FKiiiinda looks like they're okay, though.\x01",
            "They sure haven't changed too much!\x02\x03",

            "I gotta admit I'm having trouble imagining\x01",
            "what their travels together are like, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        (
            "#027FAnelace has a very straightforward,\x01",
            "open personality.\x02\x03",

            "She actually makes a good contrast to\x01",
            "Agate's quiet, moody determination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x107,
        "#063F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #142
        0x101,
        "#1004F#4PTita?\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #143
        0x107,
        "#065FEep!\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x107, 180, 600)

    ChrTalk(    #144
        0x107,
        "#067FHuh, what, who?! Estelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1015F#4PWhat's up? You're kind of spacing out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x107,
        (
            "#560FUm, um, was I?\x02\x03",

            "I was just, um, surprised, is all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1004F#4PSurprised? At what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x107,
        (
            "#065FUm, well, um...\x02\x03",

            "#067FI, um...didn't know Agate had a girlfriend!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#1004F#4PG-G-Girlfr...\x01",
            "You mean ANELACE?!\x02\x03",

            "#1016FPFFFAAAHAHAHA! No waaaaaay!\x01",
            "They're just partners on a job, Tita!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x107,
        "#064FWha?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x103,
        (
            "#027FYou see, Tita, we split into\x01",
            "teams to investigate the society in\x01",
            "multiple parts of Liberl at once.\x02\x03",

            "She's watching his back, not whispering\x01",
            "sweet nothings into his ear.\x01",
            "Heh... That IS a concept...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x107,
        (
            "#560FO-Oooh! I get it!\x02\x03",

            "#067FYeah, that is...kinda funny...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#1016F#4P(Funny...\x01",
            "Aw, I bet it isn't for you, Tita...)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)
    Sleep(400)

    ChrTalk(    #154
        0x101,
        (
            "#1015F#6PStill, though...remnants of the bandits\x01",
            "AND the Intelligence goons...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 225, 400)

    ChrTalk(    #155
        0x103,
        (
            "#020FBoth groups do seem to be involved\x01",
            "with the society in some way.\x02\x03",

            "With a bit of luck, Agate and Anelace\x01",
            "should find us some useful clues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1006F#6PWe'd better do our best, too.\x02\x03",

            "#1011FAnyway...right here is fine, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D79")

    ChrTalk(    #157
        0x103,
        (
            "#027FIt should be.\x01",
            "Let's go set up the other two instruments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1006F#6PRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC2")

    label("loc_4D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DF5")

    ChrTalk(    #159
        0x103,
        (
            "#526FThat's two instruments in place,\x01",
            "either way.\x02\x03",

            "Shall we go place the last one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#1006F#6POkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC2")

    label("loc_4DF5")


    ChrTalk(    #161
        0x103,
        (
            "#026FYes, and that's the last instrument\x01",
            "in place.\x02\x03",

            "#020FLet's return to the Operations room in the\x01",
            "factory and check in with Professor Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1006F#6PRight. Fifth floor of the factory!\x02",
    )

    CloseMessageWindow()
    OP_28(0x87, 0x1, 0x200)

    label("loc_4EC2")

    OP_64(0x0, 0x1)
    OP_A2(0x141B)
    OP_28(0x87, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_7_C8B end

    def Function_8_4ED2(): pass

    label("Function_8_4ED2")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F4B"),
        (1, "loc_4F51"),
        (SWITCH_DEFAULT, "loc_4F57"),
    )


    label("loc_4F4B")

    OP_A2(0x1200)
    Jump("loc_4F57")

    label("loc_4F51")

    OP_A2(0x1201)
    Jump("loc_4F57")

    label("loc_4F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4F65")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4F69")

    label("loc_4F65")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4F69")

    Return()

    # Function_8_4ED2 end

    def Function_9_4F6A(): pass

    label("Function_9_4F6A")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4FA4")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_4FBE")

    label("loc_4FA4")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_4FBE")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_4F6A end

    def Function_10_4FD0(): pass

    label("Function_10_4FD0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5065")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x150, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5020")

    AnonymousTalk(    #163
        "\x07\x05It's too dark to see clearly.\x02",
    )

    Jump("loc_504A")

    label("loc_5020")


    AnonymousTalk(    #164
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )


    label("loc_504A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_5220")

    label("loc_5065")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #165
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5205")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x2, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, 284880, 1050, -26870, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_73(0x11)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 284880, 1050, -26870, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, 284880, 1050, -26870, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_5205")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_521F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_521F")

    Return()

    label("loc_5220")

    Return()

    # Function_10_4FD0 end

    def Function_11_5221(): pass

    label("Function_11_5221")

    EventBegin(0x1)

    ChrTalk(    #166
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_524D():
        OP_6D(268050, -1000, -27370, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_524D)

    def lambda_5265():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5265)

    def lambda_5275():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_5275)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #167
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5339")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_C0(0xE, 0x1E, 0x4160E, 0x0, 0xFFFF8CC4, 0x0, 0x41834, 0xFFFFFAEC, 0xFFFF9BCE)
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    EventEnd(0x1)
    Jump("loc_5348")

    label("loc_5339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5348")
    EventEnd(0x1)

    label("loc_5348")

    Return()

    # Function_11_5221 end

    SaveToFile()

Try(main)
