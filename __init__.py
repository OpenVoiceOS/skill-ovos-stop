# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from ovos_utils import classproperty
from ovos_utils.process_utils import RuntimeRequirements
from ovos_workshop.decorators import fallback_handler, intent_handler
from ovos_workshop.skills.fallback import FallbackSkill


class StopSkill(FallbackSkill):

    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(internet_before_load=False,
                                   network_before_load=False,
                                   gui_before_load=False,
                                   requires_internet=False,
                                   requires_network=False,
                                   requires_gui=False,
                                   no_internet_fallback=True,
                                   no_network_fallback=True,
                                   no_gui_fallback=True)

    @intent_handler("stop.intent")
    def handle_stop(self, message):
        self.bus.emit(message.reply("mycroft.stop", {}))

    @intent_handler("global_stop.intent")
    def handle_global_stop(self, message):
        # TODO - implement the "different stops" in core
        # - go trough TTS -> active skill list -> global stop (current behavior)
        # try to stop by order until one does (this allows to for eg, stop wikipedia + keep music playing in background)
        # self.bus.emit(message.reply("mycroft.stop.global", {}))
        self.bus.emit(message.reply("mycroft.stop", {}))

    @fallback_handler(priority=80)
    def handle_fallback(self, message):
        utterance = message.data.get("utterance", "")
        if self.voc_match(utterance, 'StopKeyword'):
            self.bus.emit(message.reply("mycroft.stop", {}))
            return True
        return False
