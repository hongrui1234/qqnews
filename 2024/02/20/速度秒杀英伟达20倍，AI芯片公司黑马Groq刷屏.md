# 速度秒杀英伟达20倍，AI芯片公司黑马Groq刷屏

![efb50d214fb726256d3c049b17111eba.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/02/20/速度秒杀英伟达20倍，AI芯片公司黑马Groq刷屏/efb50d214fb726256d3c049b17111eba.jpg)

![16b5b2910bcc8b6a683194f3d3243bbb.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/02/20/速度秒杀英伟达20倍，AI芯片公司黑马Groq刷屏/16b5b2910bcc8b6a683194f3d3243bbb.jpg)

文/ 腾讯科技 郝博阳 金鹿

财报发布前两天，英伟达突然冒出来一个劲敌。

一家名叫Groq的公司今天在AI圈内刷屏，杀招就一个：快。

在传统的生成式AI中，等待是稀松平常的事情，字符一个个蹦出，半天才能回答完毕。但在Groq今天开放的云服务体验平台上，你看到的会是一秒一屏。当模型收到提示后，几乎能够立即生成答案。这些答案不仅真实可信，还附有引用，长度更是达到数百个单词。

电子邮件初创企业Otherside AI的首席执行官兼联合创始人马特·舒默（Matt
Shumer）在演示中亲自体验了Groq的强大功能。他称赞Groq快如闪电，能够在不到一秒钟的时间内生成数百个单词的事实性、引用性答案。更令人惊讶的是，它超过3/4的时间用于搜索信息，而生成答案的时间却短到只有几分之一秒。

虽然今天才刷屏，但Groq公司并非初出茅庐的新创企业。实际上，该公司成立于2016年，并在那时就注册了Groq商标。去年11月，当马斯克发布人工智能模型Grok时，Groq公司的开发者们就发了一篇文章说马斯克撞名自己的公司。信写的挺逗的，但这波流量他们是一点没吃到。

![5c6efc56a3ec8ab7216675b0090dae6f.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/02/20/速度秒杀英伟达20倍，AI芯片公司黑马Groq刷屏/5c6efc56a3ec8ab7216675b0090dae6f.jpg)

这一回他们之所以能突然爆发，主要是因为Groq云服务的上线，让大家真的能亲身感受一下不卡顿的AI用起来有多爽，或者说有多吓人。

有从事人工智能开发的用户称赞，Groq是追求低延迟产品的“游戏规则改变者”，低延迟指的是从处理请求到获得响应所需的时间。另一位用户则表示，Groq的LPU在未来有望对GPU在人工智能应用需求方面实现“革命性提升”，并认为
**它可能成为英伟达A100和H100芯片的“高性能硬件”的有力替代品。**

加速马达LPU技术

根据其模型的首次公开基准测试结果，它云服务搭载的Llama2或Mistreal模型在计算和响应速度上远超ChatGPT。这一卓越性能的背后，是Groq团队为大语言模型（LLM）量身定制的专用芯片（ASIC），它使得Groq每秒可以生成高达500个
token。相比之下，目前ChatGPT-3.5的公开版本每秒只能生成大约40个token。

![07efb12c2c5ead5ccc541bcecea62531.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/02/20/速度秒杀英伟达20倍，AI芯片公司黑马Groq刷屏/07efb12c2c5ead5ccc541bcecea62531.jpg)

Groq公司声称，他们创造了第一个语言处理单元（LPU）来运行该模型，而不是通常用于运行人工智能模型的稀缺且昂贵的图形处理单元（GPU）。

根据推特上与Groq关系密切的投资人k_zeroS分享，不同于Nvidia
GPU需要依赖高速数据传输，Groq的LPU在其系统中没有采用高带宽存储器（HBM）。它使用的是SRAM，其速度比GPU所用的存储器快约20倍。

![46cd34267dabaf295d76174dec846f5a.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/02/20/速度秒杀英伟达20倍，AI芯片公司黑马Groq刷屏/46cd34267dabaf295d76174dec846f5a.jpg)

鉴于AI的推理计算相较于模型训练需要的数据量远小，Groq的LPU因此更节能。在执行推理任务时，它从外部内存读取的数据更少，消耗的电量也低于Nvidia的GPU。

LPU的工作原理与GPU截然不同。它采用了时序指令集计算机（Temporal Instruction Set
Computer）架构，这意味着它无需像使用高带宽存储器（HBM）的GPU那样频繁地从内存中加载数据。这一特点不仅有助于避免HBM短缺的问题，还能有效降低成本。

如果在AI处理场景中采用Groq的LPU，可能就无需为Nvidia
GPU配置特殊的存储解决方案。LPU并不像GPU那样对存储速度有极高要求。Groq公司宣称，其技术能够通过其强大的芯片和软件，在AI任务中取代GPU的角色。

传奇CEO，小团队

Groq虽然默默无闻，但背后的团队可是人才济济。CEO是可被称为“TPU之父”的前谷歌员工乔纳森·罗斯；联合创始人道格拉斯·怀特曼也来自谷歌TPU团队，并先后创立了四家公司。该公司首席技术官吉姆·米勒曾是亚马逊云计算服务AWS设计算力硬件的负责人，CMO曾主导了苹果Macintosh的市场发布。

![22074324a7cc26497e2631318dc85abf.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/02/20/速度秒杀英伟达20倍，AI芯片公司黑马Groq刷屏/22074324a7cc26497e2631318dc85abf.jpg)

_（乔纳森·罗斯）_

他的总部位于加州山景城，该公司仅有180余名员工，甚至还不到英特尔等大型芯片制造商所需工程师数量的四分之一。

罗斯等人的目标是在Groq复制他在谷歌的成功经验，打造一个内部芯片项目，引领整个行业向新技术迈进。然而，这次他将面临更为激烈的市场竞争，不仅要在估值高达4700亿美元的芯片行业中与巨头竞争，还要与众多拥有新颖解决方案的新创企业一较高下。

Groq坚信其芯片将吸引大型数据中心运营商的青睐。凭借其可预测的性能和高效能耗比，Groq的组件有助于数据中心运营商实现更精细的规划和电力节约。此外，这些特性在动力有限的自动驾驶汽车中同样具有重要意义。

罗斯坚称，Groq无意被收购。相反，他希望吸引少数关键客户，通过广泛部署Groq芯片为公司提供稳定的收入来源，推动公司的独立发展。目前，这家初创公司已开始向潜在客户发送样品。

“这就像猎杀大象，”罗斯说道，“你只需要少数猎物就能维持自己的生命，尤其在我们还如此弱小的时候。”

