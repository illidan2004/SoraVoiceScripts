from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4240   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4240.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Queen Alicia',                         # 9
        '1st Lieutenant Schwarz',               # 10
        'Joshua',                               # 11
        'Olivier',                              # 12
        'Zin',                                  # 13
        'Special Ops Soldier',                  # 14
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH02010 ._CH',             # 03
        'ED6_DT07/CH02090 ._CH',             # 04
        'ED6_DT07/CH00010 ._CH',             # 05
        'ED6_DT07/CH00030 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT07/CH01330 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH02010P._CP',             # 03
        'ED6_DT07/CH02090P._CP',             # 04
        'ED6_DT07/CH00010P._CP',             # 05
        'ED6_DT07/CH00030P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT07/CH01330P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 11510,
        Z                   = 0,
        Y                   = -154850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 11510,
        Y                   = -1000,
        Z                   = -154850,
        Range               = 4000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = -102000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = -102000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_25B",          # 01, 1
        "Function_2_2AF",          # 02, 2
        "Function_3_475",          # 03, 3
        "Function_4_78A",          # 04, 4
        "Function_5_935",          # 05, 5
        "Function_6_AAD",          # 06, 6
        "Function_7_C25",          # 07, 7
        "Function_8_C7F",          # 08, 8
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_20D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_224")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 3)

    label("loc_224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24E")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_END)), "loc_25A")
    SetChrFlags(0xD, 0x80)

    label("loc_25A")

    Return()

    # Function_0_1F6 end

    def Function_1_25B(): pass

    label("Function_1_25B")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_286")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x1, 0x0, 0x5)
    OP_1B(0x3, 0x0, 0x6)
    OP_6F(0x0, 120)

    label("loc_286")

    OP_72(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A5")
    OP_64(0x0, 0x1)
    OP_71(0x1, 0x10)
    OP_1C(0x1, 0x0, 0x8)

    label("loc_2A5")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_25B end

    def Function_2_2AF(): pass

    label("Function_2_2AF")

    EventBegin(0x0)
    OP_6D(9400, 0, -139720, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    RemoveParty(0x0, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x4, 0xFF)
    AddParty(0x1, 0xFF)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    SetChrPos(0x102, 14480, -1000, -140500, 270)
    SetChrPos(0x104, 14480, -1000, -140500, 270)
    SetChrPos(0x108, 14480, -1000, -140500, 270)
    SetChrFlags(0xD, 0x80)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_73(0x0)
    OP_6F(0x0, 120)
    OP_72(0x0, 0x10)
    OP_1D(0x59)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x800)

    def lambda_36B():
        OP_8E(0xFE, 0x2742, 0x0, 0xFFFDDFB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36B)
    Sleep(500)

    def lambda_38B():
        OP_8E(0xFE, 0x2562, 0x0, 0xFFFDDBA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38B)
    Sleep(500)

    def lambda_3AB():
        OP_8E(0xFE, 0x2BFC, 0x0, 0xFFFDDD0C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3AB)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 90, 400)

    ChrTalk(    #0
        0x102,
        (
            "#012FThe castle gate controls are\x01",
            "in the Royal Guard office!\x02\x03",

            "South stairs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x108,
        "#076FGot it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x108, 400)

    ChrTalk(    #2
        0x104,
        "#6P#035FLet's get going!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x660)
    OP_1B(0x1, 0x0, 0x5)
    OP_1B(0x3, 0x0, 0x6)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_2AF end

    def Function_3_475(): pass

    label("Function_3_475")

    EventBegin(0x0)
    OP_6D(50, 0, -115650, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(1450, 0)
    OP_6C(41000, 0)
    OP_6E(563, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, 0, 0, -103700, 0)
    SetChrPos(0x101, -1960, 0, -104120, 83)
    SetChrPos(0x8, 1550, 0, -103430, 281)
    SetChrPos(0x9, 1310, 0, -104570, 330)
    SetChrPos(0x105, 2540, 0, -103830, 273)
    SetChrPos(0xB, -460, 0, -105370, 12)
    SetChrPos(0xC, 710, 0, -106060, 348)
    SetChrPos(0x103, -1580, 0, -105070, 40)
    FadeToBright(2000, 0)
    OP_6D(10, 0, -103450, 4000)

    ChrTalk(    #3
        0xA,
        (
            "#012F#4PNo doubt about it...\x02\x03",

            "There are signs that someone\x01",
            "came through here recently...\x01",
            "and frequently, at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#022F#6PThat's not all...\x02\x03",

            "The tracks also suggest that\x01",
            "someone brought in something\x01",
            "very heavy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#094FI hold the key to this room, but there\x01",
            "is a spare. It's likely that's what was\x01",
            "used to gain entry.\x02\x03",

            "#092FIt would seem that we\x01",
            "must investigate.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xB4, 0x0, 0xFFFE6F74, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Queen Alicia produced a key from her dress.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4241   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_475 end

    def Function_4_78A(): pass

    label("Function_4_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_934")
    EventBegin(0x1)
    OP_4A(0xD, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86F")
    TurnDirection(0xD, 0x0, 400)

    ChrTalk(    #7
        0xD,
        (
            "Well, well. Madame Hilda. What\x01",
            "are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "As you know, this area is restricted.\x01",
            "No civilians are allowed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xD,
        (
            "If you have no official business,\x01",
            "you'd best be on your way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_86F")

    TurnDirection(0xD, 0x0, 400)

    ChrTalk(    #10
        0xD,
        "This is a restricted area.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        (
            "Suspicious individuals can and will\x01",
            "be arrested on the spot...so watch\x01",
            "yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EE")

    Fade(1000)
    SetChrPos(0x0, 9440, 0, -153980, 270)
    SetChrPos(0x1, 9440, 0, -153980, 270)
    SetChrPos(0x2, 9440, 0, -153980, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x1)
    OP_4B(0xD, 255)

    label("loc_934")

    Return()

    # Function_4_78A end

    def Function_5_935(): pass

    label("Function_5_935")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_997")

    ChrTalk(    #12
        0x102,
        (
            "#012FThe castle gate controls are\x01",
            "in the Royal Guard office.\x02\x03",

            "South stairs!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A91")

    label("loc_997")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A20")
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(    #13
        0x102,
        (
            "#012FThe castle gate controls are\x01",
            "in the Royal Guard office!\x02\x03",

            "South stairs!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 400)

    ChrTalk(    #14
        0x104,
        "#035FLet's get going!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A91")

    label("loc_A20")

    TurnDirection(0x102, 0x108, 400)

    ChrTalk(    #15
        0x102,
        (
            "#012FThe castle gate controls are\x01",
            "in the Royal Guard office!\x02\x03",

            "South stairs!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x102, 400)

    ChrTalk(    #16
        0x108,
        "#072FGot it!\x02",
    )

    CloseMessageWindow()

    label("loc_A91")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_5_935 end

    def Function_6_AAD(): pass

    label("Function_6_AAD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0F")

    ChrTalk(    #17
        0x102,
        (
            "#012FThe castle gate controls are\x01",
            "in the Royal Guard office!\x02\x03",

            "South stairs!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_B0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B98")
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(    #18
        0x102,
        (
            "#012FThe castle gate controls are\x01",
            "in the Royal Guard office!\x02\x03",

            "South stairs!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 400)

    ChrTalk(    #19
        0x104,
        "#035FLet's get going!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_B98")

    TurnDirection(0x102, 0x108, 400)

    ChrTalk(    #20
        0x102,
        (
            "#012FThe castle gate controls are\x01",
            "in the Royal Guard office!\x02\x03",

            "South stairs!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x102, 400)

    ChrTalk(    #21
        0x108,
        "#072FGot it!\x02",
    )

    CloseMessageWindow()

    label("loc_C09")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_6_AAD end

    def Function_7_C25(): pass

    label("Function_7_C25")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x05The entrance is firmly sealed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_C25 end

    def Function_8_C7F(): pass

    label("Function_8_C7F")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_8_C7F end

    SaveToFile()

Try(main)
