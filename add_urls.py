#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 企業URLマッピング
urls = {
    21: "https://fce-hd.co.jp/",
    22: "https://corp.opro.net/",
    23: "https://www.a-job.dev/",
    24: "https://autoro.io/",
    25: "https://datasyncer.craftex.jp/company",
    26: "https://create-new-air.com/",
    27: "https://www.crosshead.co.jp/",
    28: "https://www.grop-sc.jp/",
    29: "https://gbalb.com/",
    30: "https://line-works.com/",
    31: "https://kandi-sol.co.jp/",
    32: "https://www.adobe.com/jp/",
    33: "https://www.kddi-webcommunications.co.jp/",
    34: "https://www.vonagebusiness.jp/",
    35: "https://www.comture.com/",
    36: "https://corp.collabo-style.co.jp/",
    37: "https://www.contract-mgt.jp/",
    38: "https://www.fujifilm.com/ffis/ja",
    39: "https://samurai-sys.com/",
    40: "",  # 公式サイトなし
    41: "https://jp.corp-sansan.com/",
    42: "https://www.systems.nakashima.co.jp/",
    43: "https://www.shanon.co.jp/",
    44: "https://www.stec.co.jp/",
    45: "https://www.cdata.com/jp/",
    46: "https://www.c-rise.co.jp/",
    47: "https://j-barrel.jp/",
    48: "https://www.japacom.co.jp/",
    49: "https://www.globalsign.co.jp/",
    50: "https://www.gmogshd.com/",
    51: "https://www.skygroup.jp/",
    52: "https://star-system.jp/",
    53: "https://3-shake.com/",
    54: "https://www.sonicgarden.jp/",
    55: "https://www.softcreate.co.jp/",
    56: "https://www.techvan.co.jp/",
    57: "https://japan-ai.co.jp/",
    58: "https://toma.co.jp/",
    59: "https://toyokumo-connect.com/",
    60: "https://www.docusign.com/ja-jp",
    61: "https://novelworks.jp/",
    62: "https://corp.pca.jp/",
    63: "https://will-vision.co.jp/",
    64: "https://www.fujielectric.co.jp/fsl/index.html",
    65: "https://www.progress-all.co.jp/",
    66: "https://pepacomi.com/",
    67: "https://www.box.com/ja-jp/home",
    68: "https://www.marble-corp.co.jp/",
    69: "https://www.unifinity.co.jp/",
    70: "https://umeecorp.com/",
    71: "https://usonar.co.jp/",
    72: "https://www.rakus.co.jp/",
    73: "https://www.ryobi.co.jp/",
    74: "https://www.iandc.co.jp/",
    75: "https://www.ictso.jp/",
    76: "https://www.polarit.co/",
    77: "https://www.itfit.co.jp/",
    78: "https://aibri.co.jp/",
    79: "https://www.icon-co.jp/",
    80: "https://adiem.jp/",
    81: "https://www.isr.co.jp/",
    82: "https://corp.infomart.co.jp/",
    83: "https://corp.wingarc.com/",
    84: "https://www.nttd-bb.com/",
    85: "https://www.ndisol.jp/",
    86: "https://www.emxas.co.jp/",
    87: "https://capcloud.co.jp/",
    88: "https://www.canon-electec.co.jp/",
    89: "https://gibbon-s.com/",
    90: "https://www.qualica.co.jp/",
    91: "https://company.qloba.com/",
    92: "https://coopel.ai/",
    93: "https://goodoro.co.jp/",
    94: "https://www.icds.co.jp/",
    95: "https://www.kokuyo.com/",
    96: "https://www.colife.co.jp/",
    97: "https://www.gotop.co.jp/",
    98: "https://saccsy.com/",
    99: "https://sakura-home.group/",
    100: "https://www.satirise.co.jp/",
    101: "https://www.showcase-tv.com/",
    102: "https://www.jaldx.co.jp/",
    103: "https://www.strategit.jp/",
    104: "https://thrivex.co.jp/",
    105: "https://zeroni.co.jp/",
    106: "https://sourcenext.co.jp/",
    107: "https://www.dunksoft.com/",
    108: "https://www.choidigi.com/",
    109: "https://teps.io/",
    110: "https://www.deloitte.com/jp/ja/about/group/deloitte-tohmatsu-smooth.html",
    111: "https://www.tonichi-printing.co.jp/",
    112: "https://www.e-toms.com/",
    113: "https://www.trente.jp/",
    114: "https://www.natos.jp/",
    115: "https://g-nishioka.co.jp/nishiki/",
    116: "https://www.worksap.co.jp/",
    117: "https://www.nisseicom.co.jp/",
    118: "https://www.nippon-rad.co.jp/",
    119: "https://www.neoscorp.jp/",
    120: "https://corp.netprotections.com/",
    121: "https://www.hammock.jp/",
    122: "https://www.birds.co.jp/",
    123: "https://www.pasona.co.jp/",
    124: "https://www.persol-bd.co.jp/",
    125: "https://www.hke.jp/",
    126: "https://corporate.resocia.jp/",
    127: "https://www.biztex.co.jp/",
    128: "https://bitriver.jp/",
    129: "https://ba-c.co.jp/",
    130: "https://fistbump.co.jp/",
    131: "https://www.fcs.co.jp/",
    132: "https://www.funaisoken.co.jp/",
    133: "https://flexas-z.com/",
    134: "https://cocoo.co.jp/",
    135: "https://benemo.jp/",
    136: "https://www.bengo4.com/corporate/",
    137: "https://bansonavi.com/",
    138: "https://mapple.com/",
    139: "https://mutual-growth.com/",
    140: "https://www.moved.co.jp/",
    141: "https://www.media4u.co.jp/",
    142: "https://www.usen-smartworks.co.jp/",
    143: "https://corp-link.co.jp/",
    144: "https://recomot.co.jp/",
    145: "https://www.logical-studio.com/",
    146: "https://www.worksid.co.jp/",
}

# READMEファイルを読み込む
with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 新しいコンテンツを作成
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    
    # 企業番号を検出
    if line.strip().isdigit():
        company_num = int(line.strip())
        if company_num in urls and 21 <= company_num <= 146:
            # 次の行（空行）
            i += 1
            if i < len(lines):
                new_lines.append(lines[i])
            
            # 企業名の行
            i += 1
            if i < len(lines):
                new_lines.append(lines[i])
            
            # URL行を追加（事業内容の前に挿入）
            if urls[company_num]:  # URLが空でない場合のみ
                new_lines.append(f"URL: {urls[company_num]}\n")
            else:  # キムタクなど、URLがない場合
                new_lines.append("URL: （公式サイト未確認）\n")
    
    i += 1

# ファイルに書き込む
with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("URLを追加しました")
