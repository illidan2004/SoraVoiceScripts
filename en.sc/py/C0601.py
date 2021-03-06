from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0601   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0601.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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


    DeclActor(
        TriggerX            = 16750,
        TriggerZ            = 0,
        TriggerY            = 57710,
        TriggerRange        = 1700,
        ActorX              = 16750,
        ActorZ              = 2500,
        ActorY              = 57710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 46510,
        TriggerZ            = 0,
        TriggerY            = 67900,
        TriggerRange        = 1700,
        ActorX              = 46510,
        ActorZ              = 2500,
        ActorY              = 67900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53050,
        TriggerZ            = 0,
        TriggerY            = 92420,
        TriggerRange        = 1700,
        ActorX              = 53050,
        ActorZ              = 2500,
        ActorY              = 92420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_117",          # 01, 1
        "Function_2_17A",          # 02, 2
        "Function_3_30C",          # 03, 3
        "Function_4_33B",          # 04, 4
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Return()

    # Function_0_116 end

    def Function_1_117(): pass

    label("Function_1_117")

    OP_72(0x0, 0x28)
    OP_72(0x1, 0x28)
    OP_72(0x2, 0x28)
    OP_72(0x3, 0x28)
    OP_72(0x4, 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_145")
    OP_6F(0x7, 60)
    OP_6F(0x0, 260)

    label("loc_145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15A")
    OP_6F(0x7, 60)
    OP_6F(0x0, 260)

    label("loc_15A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_16F")
    OP_6F(0x0, 60)
    OP_6F(0x4, 260)

    label("loc_16F")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_117 end

    def Function_2_17A(): pass

    label("Function_2_17A")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)

    AnonymousTalk(    #0
        "There is a lever. Move it?\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25C")

    Menu(
        0,
        260,
        200,
        0,
        (
            "Drop To The Right\x01",      # 0
            "Drop To The Left\x01",       # 1
            "Don't Move\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20F")
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    OP_73(0x2)
    OP_A2(0x0)
    Jump("loc_230")

    label("loc_20F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230")
    OP_6F(0x2, 100)
    OP_70(0x2, 0xA0)
    OP_73(0x2)
    OP_A2(0x1)

    label("loc_230")

    OP_6D(52660, -60, 67850, 500)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_69(0x0, 0x258)
    Jump("loc_303")

    label("loc_25C")


    Menu(
        0,
        260,
        200,
        0,
        (
            "Return To Original Position\x01",      # 0
            "Don't Move\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2BF")
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    OP_A3(0x0)
    Jump("loc_2DA")

    label("loc_2BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DA")
    OP_6F(0x2, 160)
    OP_70(0x2, 0x64)
    OP_73(0x2)
    OP_A3(0x1)

    label("loc_2DA")

    OP_6D(52660, -60, 67850, 500)
    OP_6F(0x1, 120)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_69(0x0, 0x258)

    label("loc_303")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_2_17A end

    def Function_3_30C(): pass

    label("Function_3_30C")

    TalkBegin(0xFF)

    AnonymousTalk(    #1
        "ダミーです。モンスターが降って来た！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_3_30C end

    def Function_4_33B(): pass

    label("Function_4_33B")

    SetMapFlags(0x80)
    ClearMapFlags(0x1)

    AnonymousTalk(    #2
        "There is a lever. Move it?\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD")

    Menu(
        0,
        260,
        200,
        0,
        (
            "Drop\x01",            # 0
            "Don't Move\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    EventBegin(0x0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xFA)
    OP_73(0x4)
    OP_A2(0x2)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    label("loc_3BD")


    Menu(
        0,
        260,
        200,
        0,
        (
            "Raise\x01",           # 0
            "Don't Move\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    EventBegin(0x0)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_6F(0x4, 250)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_A3(0x2)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    # Function_4_33B end

    SaveToFile()

Try(main)
