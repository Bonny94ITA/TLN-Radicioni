from gensim.summarization.summarizer import summarize
import gensim
import logging


logger = logging.getLogger("gensim")
logger.disable()
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

#logging.getLogger().setLevel(logging.WARNING)

text = '''Donald Trump vs Barack Obama on Nuclear Weapons in East Asia
...Donald Trump broke a lot of foreign-policy crockery last week. President Barack Obama dressed him down for encouraging South Korea and Japan to acquire nuclear weapons. NATO’s secretary-general, Jens Stoltenberg, has criticized him too. Academics trying to parse Mr. Trump’s statements can’t figure out which “school” of foreign-policy thinking he belongs to. (So far, my favorite scholarly comment has been: “There is no indication that Trump understands the workings of balance of power theory…” Of course, there is no indication that Mr. Trump cares about the workings of any theories—and no real danger that he subscribes to them.)
...The candidate’s set-to with the president, however, was far from frivolous. Mr. Trump suggested that, if South Korea and Japan had nuclear weapons, we could spend less protecting those allies. This approach, Mr. Obama rejoined, would reverse decades of U.S. policy on nuclear proliferation. (One of the president’s aides said it would be “catastrophic.”) The president was particularly indignant after the success of last week’s Nuclear Security Summit—at which he got Poland and Kazakhstan to agree to reduce their stockpiles of enriched uranium, Japan to ship out some separated plutonium, and other participants to tighten up a treaty on securing nuclear materials.
...These were worthy achievements. Yet Mr. Trump has—okay, maybe unwittingly—highlighted a question about the entire non-proliferation enterprise that is at least as important as anything that happened at Mr. Obama’s summit.
...In the half-century since the nuclear Non-Proliferation Treaty was negotiated, no state has gotten nuclear weapons because materials for doing so were inadequately secured. For all new nuclear powers (and those countries that decided not to go nuclear, such as Germany, Ukraine, and South Africa), the decisive factor was how they saw the main threats to their own security. Mr. Trump is right about one thing: The big question raised by North Korea’s success in building a nuclear arsenal is whether South Korea and Japan feel obliged to follow suit.
...There is a terrible irony in thinking through how to avoid this result. Only one country—China—may be able to get the North Koreans to change course. Beijing’s record on this issue, while improving, remains inadequate. China has usually failed to deliver the pressure it promises. Yet there is one thing that might get Beijing to do better: the Trumpian prospect that Seoul and Tokyo will decide to become nuclear powers. No U.S. president should want them to do so—or take for granted that he or she could stop them. China needs to reckon with, and be reminded of, the enormous danger it is courting. Whatever he understands about the workings of balance-of-power theory, Donald Trump has provided one such reminder. He may do more good than he knows.
'''
print(summarize(text))