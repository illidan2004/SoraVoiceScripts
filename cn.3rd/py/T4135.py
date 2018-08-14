from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4135   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4135.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '莉西娅',                               # 9
        '馆长',                                 # 10
        '森特',                                 # 11
        '威尔玛',                               # 12
        '',                                     # 13
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01490 ._CH',             # 01
        'ED6_DT07/CH01660 ._CH',             # 02
        'ED6_DT07/CH01430 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01490P._CP',             # 01
        'ED6_DT07/CH01660P._CP',             # 02
        'ED6_DT07/CH01430P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = -5910,
        Direction           = 255,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 0,
        Y                   = 67620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -69590,
        Z                   = 0,
        Y                   = -2210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -69580,
        Z                   = 0,
        Y                   = -580,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = 2580,
        TriggerZ            = 0,
        TriggerY            = -5970,
        TriggerRange        = 800,
        ActorX              = 4400,
        ActorZ              = 1700,
        ActorY              = -5910,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5090,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 5090,
        ActorZ              = 800,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7840,
        TriggerZ            = 4000,
        TriggerY            = 6700,
        TriggerRange        = 800,
        ActorX              = 7840,
        ActorZ              = 5700,
        ActorY              = 6700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75860,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 75860,
        ActorZ              = 1500,
        ActorY              = -2000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73200,
        TriggerZ            = 0,
        TriggerY            = 710,
        TriggerRange        = 800,
        ActorX              = 73200,
        ActorZ              = 800,
        ActorY              = 710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68740,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 68740,
        ActorZ              = 800,
        ActorY              = 7310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73480,
        TriggerZ            = 0,
        TriggerY            = 6420,
        TriggerRange        = 800,
        ActorX              = 73480,
        ActorZ              = 800,
        ActorY              = 6420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75820,
        TriggerZ            = 4000,
        TriggerY            = 8010,
        TriggerRange        = 800,
        ActorX              = 75820,
        ActorZ              = 5700,
        ActorY              = 8010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71960,
        TriggerZ            = 4000,
        TriggerY            = 9290,
        TriggerRange        = 800,
        ActorX              = 71960,
        ActorZ              = 4800,
        ActorY              = 9290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 0,
        TriggerY            = 77880,
        TriggerRange        = 800,
        ActorX              = -20,
        ActorZ              = 1700,
        ActorY              = 77880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -770,
        TriggerZ            = 0,
        TriggerY            = 72650,
        TriggerRange        = 800,
        ActorX              = -770,
        ActorZ              = 800,
        ActorY              = 72650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 66550,
        TriggerRange        = 1200,
        ActorX              = 7000,
        ActorZ              = 800,
        ActorY              = 66550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1770,
        TriggerZ            = 0,
        TriggerY            = 66890,
        TriggerRange        = 800,
        ActorX              = 1770,
        ActorZ              = 800,
        ActorY              = 66890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3790,
        TriggerZ            = 0,
        TriggerY            = 64959,
        TriggerRange        = 800,
        ActorX              = -3790,
        ActorZ              = 800,
        ActorY              = 64959,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_346",          # 00, 0
        "Function_1_358",          # 01, 1
        "Function_2_368",          # 02, 2
        "Function_3_37E",          # 03, 3
        "Function_4_607",          # 04, 4
        "Function_5_768",          # 05, 5
        "Function_6_92D",          # 06, 6
        "Function_7_932",          # 07, 7
        "Function_8_A7E",          # 08, 8
        "Function_9_BFE",          # 09, 9
        "Function_10_F38",         # 0A, 10
        "Function_11_10AD",        # 0B, 11
        "Function_12_11CE",        # 0C, 12
        "Function_13_12B6",        # 0D, 13
        "Function_14_1391",        # 0E, 14
        "Function_15_14A3",        # 0F, 15
        "Function_16_15BE",        # 10, 16
        "Function_17_1733",        # 11, 17
        "Function_18_18FF",        # 12, 18
        "Function_19_1A33",        # 13, 19
        "Function_20_1B25",        # 14, 20
    )


    def Function_0_346(): pass

    label("Function_0_346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_357")
    SetChrFlags(0x12, 0x10)

    label("loc_357")

    Return()

    # Function_0_346 end

    def Function_1_358(): pass

    label("Function_1_358")

    OP_B1("t4135_n")
    OP_71(0x401, 0x0)
    ExitThread()
    Return()

    # Function_1_358 end

    def Function_2_368(): pass

    label("Function_2_368")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_368")

    label("loc_37D")

    Return()

    # Function_2_368 end

    def Function_3_37E(): pass

    label("Function_3_37E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_38B")
    Jump("loc_603")

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_4B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_40D")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #0
        0xFE,
        (
            "对了，森特最近\x01",
            "也要出差去参加学术研究会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "这也就意味着这里的研究员\x01",
            "只剩下我一个人了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AF")

    label("loc_40D")


    ChrTalk(    #2
        0xFE,
        (
            "在这儿的学术人员里面，\x01",
            "威尔玛是最优秀的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "不过她很快就要被调到\x01",
            "外国的研究机构去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "虽然感觉会变得有点寂寞了，\x01",
            "但是我应该为她加油才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_4AF")

    Jump("loc_603")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_561")

    ChrTalk(    #5
        0xFE,
        (
            "利贝尔的考古学资料\x01",
            "还真是数不胜数呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "不仅从瓦雷利亚湖中发现了那么多文物，\x01",
            "而且连亚宁堡长城其实也是一个遗迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "只是知道这一点的人并不多。\x02",
    )

    CloseMessageWindow()
    Jump("loc_603")

    label("loc_561")


    ChrTalk(    #8
        0xFE,
        (
            "这个壶是上个月\x01",
            "刚从瓦雷利亚湖打捞上来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "这种花纹……\x01",
            "很可能是中世纪的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "呵呵，\x01",
            "一看到这东西，\x01",
            "连我这把老骨头也不住地激动。\x02",
        )
    )

    Jump("loc_5FF")

    label("loc_5FF")

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_603")

    TalkEnd(0xFE)
    Return()

    # Function_3_37E end

    def Function_4_607(): pass

    label("Function_4_607")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_614")
    Jump("loc_764")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_6DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_687")

    ChrTalk(    #11
        0xFE,
        (
            "『四轮之塔』在外国\x01",
            "并没有很高的知名度……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "这篇论文\x01",
            "会不会得到认可呢……\x02",
        )
    )

    Jump("loc_683")

    label("loc_683")

    CloseMessageWindow()
    Jump("loc_6DB")

    label("loc_687")


    ChrTalk(    #13
        0xFE,
        (
            "这篇论文\x01",
            "真的没问题吗。\x02",
        )
    )

    Jump("loc_6B1")

    label("loc_6B1")

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "现在开始觉得心理有些不踏实了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_6DB")

    Jump("loc_764")

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_764")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_71A")

    ChrTalk(    #15
        0xFE,
        (
            "如果能再多收集一些资料\x01",
            "就好了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_764")

    label("loc_71A")


    ChrTalk(    #16
        0xFE,
        "怎、怎么样，前辈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "嗯～\x01",
            "感觉说服力还是不太充分……\x02",
        )
    )

    Jump("loc_760")

    label("loc_760")

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_764")

    TalkEnd(0xFE)
    Return()

    # Function_4_607 end

    def Function_5_768(): pass

    label("Function_5_768")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_775")
    Jump("loc_929")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_800")

    ChrTalk(    #18
        0xFE,
        (
            "今年的考古学术研究会\x01",
            "在奥雷德自治州召开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "唉，我也好想去哦～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "可现在还有事务缠身，\x01",
            "今年只有放弃了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E")

    label("loc_800")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #21
        0xFE,
        "哼，谁会紧张啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "我才没有那么紧张呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_83E")

    Jump("loc_929")

    label("loc_841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_929")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8BA")

    ChrTalk(    #23
        0xFE,
        (
            "森特，很快你就要\x01",
            "去参加人生中第一次学术研究会了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "不过这次\x01",
            "我不能陪你去了。\x02",
        )
    )

    Jump("loc_8B6")

    label("loc_8B6")

    CloseMessageWindow()
    Jump("loc_929")

    label("loc_8BA")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #25
        0xFE,
        (
            "对了，\x01",
            "论据似乎还有一些薄弱。\x02",
        )
    )

    Jump("loc_8EE")

    label("loc_8EE")

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "虽然应该已经有不少资料了，\x01",
            "不过还是再借一些吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_929")

    TalkEnd(0xFE)
    Return()

    # Function_5_768 end

    def Function_6_92D(): pass

    label("Function_6_92D")

    Call(0, 7)
    Return()

    # Function_6_92D end

    def Function_7_932(): pass

    label("Function_7_932")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_93F")
    Jump("loc_A7A")

    label("loc_93F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_989")

    ChrTalk(    #27
        0x10,
        (
            "威尔玛下个月\x01",
            "就要去外国了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "有点寂寞呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_989")


    ChrTalk(    #29
        0x10,
        (
            "威尔玛学员\x01",
            "从下个月开始\x01",
            "就要去外国的研究机构了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        "算了，这也是没办法的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "因为他们\x01",
            "都很有才能嘛……\x02",
        )
    )

    Jump("loc_A2B")

    label("loc_A2B")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A2F")

    Jump("loc_A7A")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_A7A")

    ChrTalk(    #33
        0x10,
        (
            "欢迎光临，\x01",
            "这里是历史资料馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "请务必好好参观一下。\x02",
    )

    CloseMessageWindow()

    label("loc_A7A")

    TalkEnd(0x10)
    Return()

    # Function_7_932 end

    def Function_8_A7E(): pass

    label("Function_8_A7E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #35
        (
            "\x07\x05【『四轮之塔』的外壁】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　这块朴素的石壁，是从『大崩坏』后所建\x01",
            "的『四轮之塔』上作为研究资料切割出来的。\x01",
            "其上所绘制的纹样是同时代建筑物中的典型，\x01",
            "据说描述的是持杖的祭司，以及展翅的神祗的\x01",
            "身姿。关于其与七耀教会成立之后的代表神格\x01",
            "『空之女神』的关系，各方面的研究仍在进行\x01",
            "中。\x01",
            "　　\x02",
        )
    )

    Jump("loc_BE5")

    label("loc_BE5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_A7E end

    def Function_9_BFE(): pass

    label("Function_9_BFE")

    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D98")
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #36
        (
            "\x07\x05【七耀历１１５０～１２００年\x01",
            "　　　　　　　～导力革命以后的世界～】\x01",
            "　　Ｃ·爱普斯泰恩博士发明导力器后不到五\x01",
            "十年。世界以惊人的速度进步着，接连不断地\x01",
            "开拓岀导力技术新的应用领域。堪称其象征的\x01",
            "就是飞艇。\x01",
            "　　\x01",
            "　　利贝尔王国定期飞艇的运航已经成为国民\x01",
            "们习以为常的交通方式，近年来埃雷波尼亚帝\x01",
            "国等其它国家也开始致力于研发商用基准的飞\x01",
            "艇。\x02",
        )
    )

    Jump("loc_D80")

    label("loc_D80")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_F34")

    label("loc_D98")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #37
        (
            "\x07\x05【七耀历１１５０～１２００年\x01",
            "　　　　　　　～导力革命以后的世界～】\x01",
            "　　Ｃ·爱普斯泰恩博士发明导力器后仅仅五\x01",
            "十年。世界以惊人的速度进步着，接连不断地\x01",
            "开拓岀导力技术新的应用领域。堪称其象征的\x01",
            "就是飞艇。\x01",
            "　　\x01",
            "　　利贝尔王国定期飞艇的运航已经成为国民\x01",
            "们习以为常的交通方式，近年来埃雷波尼亚帝\x01",
            "国等其它国家也开始正式引进飞艇制造业，使\x01",
            "得飞艇级的船体逐步实用化。\x01",
            "　　\x02",
        )
    )

    Jump("loc_F1F")

    label("loc_F1F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_F34")

    TalkEnd(0xFF)
    Return()

    # Function_9_BFE end

    def Function_10_F38(): pass

    label("Function_10_F38")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #38
        (
            "\x07\x05【七耀历以前\x01",
            "　　　　　～古代塞姆里亚文明～】\x01",
            "　　距今约１２００年前，当时繁荣绝顶的塞\x01",
            "姆里亚文明突然迎来了终结，失去了文明的人\x01",
            "们开始度过漫长的暗黑时代。\x01",
            "　　\x01",
            "　　第一层的展示物据考证是『大崩坏』之后\x01",
            "所制造的遗物。虽然据判断并非古代文明的直\x01",
            "接遗物，但因受到其深刻影响，学术方面的价\x01",
            "值极高。\x01",
            "　　\x02",
        )
    )

    Jump("loc_1094")

    label("loc_1094")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_F38 end

    def Function_11_10AD(): pass

    label("Function_11_10AD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #39
        (
            "\x07\x05【古代的照明器具】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　专用于焚烧篝火的容器。在塔之类被认为\x01",
            "与祭祀仪式有关联的建筑物中频繁被使用，其\x01",
            "具体用途不仅仅是照明，在宗教上可能也拥有\x01",
            "某种程度的意义。当然这点目前还只是推测罢\x01",
            "了。  \x02",
        )
    )

    Jump("loc_11B5")

    label("loc_11B5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_10AD end

    def Function_12_11CE(): pass

    label("Function_12_11CE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #40
        (
            "\x07\x05【浮雕石柱】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　刻有优美雕刻的石柱。在瓦雷利亚湖的湖\x01",
            "底被打捞上来，可以看出与『四轮之塔』的壁\x01",
            "画类似的纹样在其上也被反复使用。\x01",
            "　　\x02",
        )
    )

    Jump("loc_129D")

    label("loc_129D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_11CE end

    def Function_13_12B6(): pass

    label("Function_13_12B6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #41
        (
            "\x07\x05【瓷工艺的地板】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　遗迹内部彩色镶嵌的瓷工艺地板。将破碎\x01",
            "的天然石块巧妙拼接，作出朴素而美妙的花纹\x01",
            "样式。\x01",
            "　　\x02",
        )
    )

    Jump("loc_1378")

    label("loc_1378")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_12B6 end

    def Function_14_1391(): pass

    label("Function_14_1391")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05【七耀历１～５００年左右\x01",
            "　　　　　　　　～暗黑时代的到来～】\x01",
            "　　由于『大崩坏』而导致文明尽失，世界陷\x01",
            "入了长期的混乱时代。\x01",
            "　　大小各异的国家、势力使得无尽的战争持\x01",
            "续了约５００年间，后世称此时代为『暗黑时\x01",
            "代』。\x02",
        )
    )

    Jump("loc_148A")

    label("loc_148A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_1391 end

    def Function_15_14A3(): pass

    label("Function_15_14A3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #43
        (
            "\x07\x05【骑士们的武具】\x01",
            "　　　　　　　　年代：七耀历５００年左右\x01",
            "　　日夜征战的时代中，战士们的集团拥有社\x01",
            "会性的强大影响力，最终成长为特权的骑士阶\x01",
            "级。\x01",
            "　　他们佩戴着如展品所示的武具投身沙场，\x01",
            "获得战利品和领土，势力不断扩大。\x01",
            "　\x02",
        )
    )

    Jump("loc_15A5")

    label("loc_15A5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_14A3 end

    def Function_16_15BE(): pass

    label("Function_16_15BE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #44
        (
            "\x07\x05【七耀历５００～１１００年左右\x01",
            "　　　　　　～七耀教会带来的安定期～】\x01",
            "　　七耀教会登上历史舞台，正值暗黑时代末\x01",
            "期，七耀历５００年左右。\x01",
            "　　以『空之女神』为中心所整理的教义，通\x01",
            "过教会救济民众的社会活动，瞬间深入人心。\x01",
            "　　它的权威很快成长到连贵族、骑士阶级也\x01",
            "无法忽视的地步，其后以教会为中心的新秩序\x01",
            "便逐步形成了。\x01",
            "　\x02",
        )
    )

    Jump("loc_171A")

    label("loc_171A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_15BE end

    def Function_17_1733(): pass

    label("Function_17_1733")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #45
        (
            "\x07\x05【古代文明的遗物——\x01",
            "　　　　　　　　『古代遗物』】\x01",
            "　　　　　　　　　　　　　　　年代：不明\x01",
            "　　『古代遗物』是从各地发现的古代遗迹中\x01",
            "出土的诸如器物、杖等形态各异、不可思议的\x01",
            "遗物。\x01",
            "　　在七耀教会的教义中，作为与女神赐予的\x01",
            "『七至宝』相关的物品，其回收成为教会必须\x01",
            "履行的义务之一。展品的『古代遗物』也是教\x01",
            "会所回收的物品。\x01",
            "　　许多传闻称其拥有超常的力量，但此展品\x01",
            "已经失去能力，无法启动。\x01",
            "　　\x02",
        )
    )

    Jump("loc_18E6")

    label("loc_18E6")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_1733 end

    def Function_18_18FF(): pass

    label("Function_18_18FF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #46
        (
            "\x07\x05【七耀教会的祭具】\x01",
            "　　　　　　　　年代：七耀历９００年左右\x01",
            "　　七耀教会创造岀种种的宗教艺术，由此开\x01",
            "始教会开拓出一个稳定的时代。据考证，『空\x01",
            "之女神』的圣像也是由此时起被塑造为现今的\x01",
            "姿态。此外，现在所使用的祭祀道具多数也是\x01",
            "在这个时代被定型的。\x01",
            "　　\x02",
        )
    )

    Jump("loc_1A1A")

    label("loc_1A1A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_18FF end

    def Function_19_1A33(): pass

    label("Function_19_1A33")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #47
        (
            "\x07\x05【七耀教会圣典的抄本】\x01",
            "　　　　　　　　年代：七耀历５００年左右\x01",
            "　　暗黑时代末期的原始七耀教会所使用的圣\x01",
            "典抄本。中世纪没有印刷技术，因此这本书是\x01",
            "由人手工抄写在兽皮制的纸张上的。\x01",
            "　　\x02",
        )
    )

    Jump("loc_1B0C")

    label("loc_1B0C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_1A33 end

    def Function_20_1B25(): pass

    label("Function_20_1B25")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #48
        (
            "\x07\x05【中世纪的纺纱机】\x01",
            "　　　　　　　　年代：七耀历９００年左右\x01",
            "　　纺纱用的手工机械。到了稳定的中世纪，\x01",
            "农民的生活逐渐富裕，作为商品作物的棉花栽\x01",
            "培日渐繁盛。为了收入货币，这个时代的手工\x01",
            "业也开始发展。\x01",
            "　　\x02",
        )
    )

    Jump("loc_1C11")

    label("loc_1C11")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_1B25 end

    SaveToFile()

Try(main)
