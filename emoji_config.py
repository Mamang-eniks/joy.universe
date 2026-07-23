r"""
JOY UNIVERSE — Emoji Configuration
===================================
Isi semua ID emoji dari server Discord lu di sini.

Cara ambil ID emoji:
1. Upload emoji ke server Discord lu
2. Di chat Discord ketik  \:nama_emoji:  (pakai backslash)
3. Send — Discord akan tampilkan format lengkapnya: <:nama:1234567890>
4. Copy angka ID-nya, paste di bawah

Format:
  - Emoji biasa  : "<:nama:ID>"
  - Emoji animasi: "<a:nama:ID>"

Contoh:
  BADGE_FOUNDER = "<:founder:1234567890123456>"
  BADGE_STAFF   = "<a:staff:9876543210987654>"   # animated
"""

# ══════════════════════════════════════════════════════════════════
# BADGE EMOJI
# ══════════════════════════════════════════════════════════════════

BADGE_FOUNDER    = "<:emoji_46:1528958923472769186>"   # Emoji untuk badge FOUNDER
BADGE_DEVELOPER  = "<:emoji_50:1528959036626567258>"   # Emoji untuk badge DEVELOPER
BADGE_MANAGEMENT = "<:emoji_47:1528958972441137202>"   # Emoji untuk badge MANAGEMENT
BADGE_STAFF      = "<:emoji_47:1528958989470269540>"   # Emoji untuk badge STAFF
BADGE_PREMIUM    = "<:premium:1528961463094612110>"   # Emoji untuk badge PREMIUM
BADGE_NOPREFIX   = "<:emoji_50:1528959055241154780>"   # Emoji untuk badge NO PREFIX
BADGE_USER       = "<:emoji_52:1528959097259688006>"   # Emoji untuk badge USER

# ══════════════════════════════════════════════════════════════════
# UI / SECTION EMOJI (untuk help, info, dll)
# ══════════════════════════════════════════════════════════════════

# Section headers di !vx help
ICON_MODERATION  = "<:emoji_52:1529987703125442700>"   # Icon untuk section Moderation
ICON_ROLE        = "<:emoji_58:1529987879802241034>"   # Icon untuk section Role & Voice
ICON_INFO        = "<:emoji_51:1529987677850702055>"   # Icon untuk section Info
ICON_TICKET      = "<:emoji_55:1529987766849376407>"   # Icon untuk section Ticket
ICON_LEVEL       = "<:emoji_35:1528930032989372708>"   # Icon untuk section Level & XP
ICON_GIVEAWAY    = "<:emoji_63:1529987959410004008>"   # Icon untuk section Giveaway
ICON_ANTISPAM    = "<:emoji_63:1529987994742816900>"   # Icon untuk section Antispam
ICON_LANGUAGE    = "<a:customize:1529656166617972938>"   # Icon untuk section Language
ICON_OWNER       = "<:emoji_49:1529987523135410196>"   # Icon untuk section Owner Only

# Status / result icons
ICON_SUCCESS     = "<:emoji_37:1528930134349058248>"   # Icon sukses (checklist, dll)
ICON_ERROR       = "<:emoji_38:1528930169950310441>"   # Icon error / gagal
ICON_WARNING     = "<:emoji_32:1528929890038972466>"   # Icon warning / peringatan
ICON_LOADING     = "<:emoji_29:1528929806392229929>"   # Icon loading / proses

# Profile card icons
ICON_PROFILE     = "<:author:1522209388537053194>"   # Icon di header profile
ICON_BADGES      = "<:Red_wal:1522215269622349999>"   # Icon di ALL BADGES
ICON_COMMANDS    = "<:settings:1522216254448992317>"   # Icon di Commands Runned
ICON_PREMIUM_TAG = "<a:emoji_773:1522210263821062301>"   # Icon di keterangan premium

# Ticket icons
ICON_TICKET_OPEN  = "<:emoji_53:1528949967207534702>"  # Icon tombol Open Ticket
ICON_TICKET_CLOSE = "<:emoji_53:1528949983645138984>"  # Icon tombol Close Ticket

# Giveaway icons
ICON_GIVEAWAY_REACT = "<a:emoji_51:1529240194920874164>" # Icon reaksi giveaway (default 🎉 kalau kosong)
ICON_WINNER          = "<a:emoji_53:1522406976632389855>" # Icon pengumuman pemenang

# ══════════════════════════════════════════════════════════════════
# HELPER FUNCTION
# ══════════════════════════════════════════════════════════════════

def e(emoji_str: str, fallback: str = "") -> str:
    """
    Return emoji kalau sudah diisi, fallback kalau masih kosong.
    Contoh: e(BADGE_FOUNDER, "👑") → "<:founder:123>" atau "👑"
    """
    return emoji_str if emoji_str.strip() else fallback
